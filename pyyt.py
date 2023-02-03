import os
from moviepy.editor import *
from pytube import YouTube
from pytube.cli import on_progress

a=YouTube('https://www.youtube.com/watch?v=x0apWO5n7D0&list=RDx0apWO5n7D0&start_radio=1&ab_channel=OneDirectionVEVO',on_progress_callback=on_progress)
b=a.streams.order_by('resolution').order_by('fps').last()
c=a.streams.get_audio_only()
b.download(r"F:\New folder",filename=f'video {b.default_filename}')
c.download(output_path=r"F:\New folder",filename=f'audio {c.default_filename}')
d=rf"F:\New folder\video {b.default_filename}"
e=rf"F:\New folder\audio {c.default_filename}"
g=rf"F:\New folder\{b.default_filename}"
videoclip = VideoFileClip(d)
audioclip = AudioFileClip(e)
video = videoclip.set_audio(audioclip)
video.write_videofile(g)
while True:
    try:
        os.remove(d)
        os.remove(e)
        break                             
    except IOError:
        break




