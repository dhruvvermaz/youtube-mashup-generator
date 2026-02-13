import os
from yt_dlp import YoutubeDL
from moviepy import VideoFileClip
from pydub import AudioSegment



def clean_folder(folder):

    if not os.path.exists(folder):
        os.makedirs(folder)
        return

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            os.remove(file_path)



def create_mashup(singer, number, duration, output_file):

    # Clean folders
    clean_folder("audio")
    clean_folder("cut_audio")

    print("Downloading songs...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': False
    }

    search = f"ytsearch{number}:{singer} official song"

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([search])

    print("Cutting audio clips...")

    for file in os.listdir("audio"):

        path = os.path.join("audio", file)

        audio = AudioSegment.from_file(path)

        trimmed = audio[:duration * 1000]

        trimmed.export(
            os.path.join("cut_audio", file.split('.')[0] + ".mp3"),
            format="mp3"
        )

    print("Merging clips...")

    final = AudioSegment.empty()

    files = sorted(os.listdir("cut_audio"))

    for file in files:

        sound = AudioSegment.from_mp3(
            os.path.join("cut_audio", file)
        )

        final += sound

    final.export(output_file, format="mp3")

    print(" Mashup created successfully!")

