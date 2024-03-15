# converts a video file into audio file. 📼🎵
# Write a program to convert 5 video files into audio files one by one in a loop,
# without using multi-threading.
# pip install moviepy

from time import time
from moviepy import editor

def convert(video_name, audio_name):
    video = editor.VideoFileClip(video_name)
    video.audio.write_audiofile(audio_name)

videos=[["input/Aram Aram.mp4", "output/Aram.mp3"],
        ["input/Ey Sareban.mp4", "output/Ey.mp3"],
        ["input/Kook.mp4", "output/koo.mp3"],
        ["input/Yek Nafas Arezouye To.mp4", "output/Yek Nafas.mp3"],
        ["input/E M E L - Holm.mp4", "output/E M E L.mp3"]
]

start_time=time()

for video, audio in videos:
    convert(video, audio)


end_time=time()

print(end_time-start_time)

#result=19.1849102973938 s