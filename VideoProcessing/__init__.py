import os
from pytube import YouTube
from moviepy.editor import *

url = 'https://www.youtube.com/watch?v=nwN2bNBSIZg'

yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
stream = yt.streams.get_highest_resolution()
stream.download()

video = VideoFileClip(stream.default_filename)
audio = video.audio
audio.write_audiofile("Duah.wav")

os.remove(stream.default_filename)

print("Audio extracted successfully!")