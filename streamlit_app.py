import streamlit as st
import os
import zipfile
import shutil
from mashup_script import run_from_web
from email_validator import validate_email, EmailNotValidError
import smtplib
from email.message import EmailMessage

st.title("Mashup Creator")

singer = st.text_input("Singer Name")
videos = st.number_input("Number of Videos", min_value=1)
duration = st.number_input("Duration (sec)", min_value=10)
email = st.text_input("Email")

if st.button("Generate Mashup"):
    if not singer or not email:
        st.error("All fields required")
    else:
        try:
            validate_email(email)
        except EmailNotValidError:
            st.error("Invalid Email")
        else:
            try:
                output_file = "mashup.mp3"
                mp3_path, temp_dir = run_from_web(
                    singer,
                    int(videos),
                    int(duration),
                    output_file
                )

                zip_path = os.path.join(temp_dir, "mashup.zip")

                with zipfile.ZipFile(zip_path, 'w') as zipf:
                    zipf.write(mp3_path, "mashup.mp3")

                msg = EmailMessage()
                msg['Subject'] = "Your Mashup"
                msg['From'] = st.secrets["MAIL_USERNAME"]
                msg['To'] = email
                msg.set_content("Your mashup is attached.")

                with open(zip_path, "rb") as f:
                    msg.add_attachment(
                        f.read(),
                        maintype='application',
                        subtype='zip',
                        filename="mashup.zip"
                    )

                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(
                        st.secrets["MAIL_USERNAME"],
                        st.secrets["MAIL_PASSWORD"]
                    )
                    server.send_message(msg)

                shutil.rmtree(temp_dir)

                st.success("Mashup sent successfully!")

            except Exception as e:
                st.error(str(e))
