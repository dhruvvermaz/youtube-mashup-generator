youtube-mashup-generator

This project is a web application designed to automatically create music mashups. It performs the following tasks:

Retrieves multiple songs from YouTube based on a selected singer

Clips a specific duration from each track

Combines the clips into a single mashup file

Packages the output into a ZIP file

Emails the mashup directly to the user

Provides optional deployment through Streamlit

Project Structure 

README

MASHUP/
│
├── __pycache__/
├── .streamlit/
│   └── secrets.toml
├── 102303119.py
├── app.py
├── mashup_script.py
├── streamlit_app.py
├── mashup.mp3
└── requirements.txt

Key Features 

README

Downloads audio from YouTube using pytubefix

Processes and edits audio with MoviePy

Automatically generates mashups

Creates ZIP files for easy download

Sends emails via Gmail SMTP

Includes both a Flask-based web service and a Streamlit interface

Ready for deployment on Streamlit Cloud

Installation 

README

Install all required dependencies with:

pip install -r requirements.txt


Or install them manually:

pip install streamlit flask flask-mail pytubefix moviepy email-validator

Gmail Configuration (Needed for Email Feature) 

README

Turn on 2-Step Verification in your Google account.

Go to Security → App Passwords and create a new password.

Add the generated 16-digit password to your application settings.

Running the Flask App Locally 

README

Set environment variables:

Windows

set MAIL_USERNAME=yourgmail@gmail.com
set MAIL_PASSWORD=your_app_password


Mac/Linux

export MAIL_USERNAME=yourgmail@gmail.com
export MAIL_PASSWORD=your_app_password


Start the application:

python app.py

Important Notes 

README

Always use a Gmail App Password for authentication.

Never publish your credentials in public repositories.

Large YouTube downloads may fail on free hosting platforms due to time limits.

This project is created primarily for academic use.

Technologies Used 

README

Python

Flask

Streamlit

MoviePy

pytubefix

Gmail SMTP

Author 

README

dhruv verma
