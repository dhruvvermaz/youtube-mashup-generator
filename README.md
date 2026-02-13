 YouTube Mashup Generator

A Python-based web application that automatically creates song mashups by collecting audio from YouTube, trimming selected portions, and combining them into a single track. The application can package the output and deliver it to users via email, making mashup creation fast and fully automated.

 Overview

The YouTube Mashup Generator is designed to simplify the process of creating music mashups. Instead of manually downloading and editing songs, this tool handles everything — from fetching audio to merging clips — through an easy-to-run web interface.

This project demonstrates practical use of Python web frameworks, audio processing, and API-based downloading, making it ideal for learning real-world software development concepts.

 Features

 Automatically searches and downloads songs from YouTube
 Extracts a fixed-length segment from each track
 Merges multiple clips into one seamless mashup
 Generates a downloadable audio file
 Option to send the mashup directly through email
 Supports both Flask and Streamlit interfaces
 Simple project structure for easy understanding and modification

 Tech Stack

Python – Core programming language

Flask – Backend web framework

Streamlit – Interactive web app version

MoviePy – Audio editing and merging

pytubefix – YouTube audio downloading

SMTP (Gmail) – Email delivery

 Project Structure
youtube-mashup-generator/
│
├── app.py                # Flask web application
├── streamlit_app.py     # Streamlit version of the app
├── mashup_script.py     # Handles downloading and mashup creation
├── requirements.txt    # Project dependencies
└── <project_file>.py   # Main execution / supporting script

 Installation

Clone the repository:

git clone https://github.com/your-username/youtube-mashup-generator.git
cd youtube-mashup-generator


Install dependencies:

pip install -r requirements.txt

 Running the Application
Run Flask Version
python app.py

Run Streamlit Version
streamlit run streamlit_app.py


After running, open the displayed local URL in your browser.

 Email Configuration (Optional)

To enable email delivery:

Enable 2-Step Verification on your Google account.

Generate a Gmail App Password from Security settings.

Set your credentials as environment variables:

Windows

set MAIL_USERNAME=your_email@gmail.com
set MAIL_PASSWORD=your_app_password


Mac/Linux

export MAIL_USERNAME=your_email@gmail.com
export MAIL_PASSWORD=your_app_password


 Never upload your email credentials to a public repository.

 Important Notes

Large downloads may fail on free hosting platforms due to timeout limits.

Use this project responsibly and respect copyright policies when downloading content.

Recommended primarily for educational and learning purposes.

 Learning Outcomes

This project helps in understanding:

Web app development with Python

Media processing workflows

File handling and automation

Third-party library integration

Deployable application design

 Author

Dhruv Verma
