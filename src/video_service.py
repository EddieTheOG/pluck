import os

import youtube_dl
import ffmpeg
from datetime import datetime


def download_yt_video(url):
    # download youtube video
    ydl_opts = {
        'nocheckcertificate': True,
        'format': '95',
        'forceurl': True,
        'simulate': True
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    with ydl:
        yt_info = ydl.extract_info(
            url,
            download=False
        )
    manifest_url = yt_info
    return manifest_url


def trim_video_file(result):
    # trim video to one frame
    stream = ffmpeg.input(result['url'])
    stream = stream.trim(start_frame=0, end_frame=1)
    base_path = os.path.dirname(__file__)
    print(base_path + 'recordings')
    path_of_video = os.path.abspath(os.path.join(base_path, '../recordings/{}.mp4'.format(datetime.now().microsecond)))
    stream = ffmpeg.output(stream, path_of_video)
    ffmpeg.run(stream)
    return base_path, path_of_video



