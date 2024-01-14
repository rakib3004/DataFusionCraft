import os
from pytube import YouTube
from moviepy.editor import *

url = 'https://www.youtube.com/watch?v=KN1sTl2FQNY'

yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
stream = yt.streams.get_highest_resolution()
stream.download()

video = VideoFileClip(stream.default_filename)
audio = video.audio
audio.write_audiofile("C:\\Users\\pc\\Music\\30.mp3")

os.remove(stream.default_filename)

print("Audio extracted successfully!")