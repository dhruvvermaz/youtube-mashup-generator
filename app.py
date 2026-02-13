import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request
from mashup import create_mashup
import os

app = Flask(__name__)
def send_email(receiver, file_path):

    EMAIL = "dverma2_be23@thapar.edu"
    PASSWORD = "cpfmtehnrupobckr"

    msg = EmailMessage()

    msg['Subject'] = "Your Mashup is Ready 🎵"
    msg['From'] = EMAIL
    msg['To'] = receiver

    msg.set_content(
        "Hello!\n\nYour mashup has been generated successfully.\nEnjoy your music 🎶"
    )

    with open(file_path, 'rb') as f:
        file_data = f.read()
        file_name = file_path.split("/")[-1]

    msg.add_attachment(
        file_data,
        maintype='audio',
        subtype='mpeg',
        filename=file_name
    )

   
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['GET', 'POST'])
def generate():

    if request.method == 'POST':

        singer = request.form['singer']
        number = int(request.form['number'])
        duration = int(request.form['duration'])
        email = request.form['email']


        output_file = f"output/{singer}_mashup.mp3"

        print("Starting mashup creation...")

        create_mashup(singer, number, duration, output_file)
        send_email(email, output_file)


        print("Mashup finished!")

        return f"Mashup created successfully! File saved at {output_file}"

    return "Use the form to generate mashup."


    singer = request.form['singer']
    number = int(request.form['number'])
    duration = int(request.form['duration'])

    output_file = f"output/{singer}_mashup.mp3"

    print("Starting mashup creation...")

    create_mashup(singer, number, duration, output_file)

    print("Mashup finished!")

    return f"Mashup created successfully! File saved at {output_file}"


if __name__ == '__main__':
    app.run(debug=True)

