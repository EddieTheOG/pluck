import cv2
import os
from datetime import datetime
import youtube_dl
import ffmpeg


def main():
    # ask user for URL
    # navigate pipto webpage
    # get html
    # parse html
    # retrieve image from yt video
    # post image to google cloud

    manifest_url = download_yt_video("https://www.youtube.com/watch?v=SCE9XWg7RJU")
    path_of_video = trim_video_file(manifest_url)
    convert_video_to_image(path_of_video)

    # retrieve_image_from_video_element(browser)


def request_url_from_user():
    url = input('Which music streaming site are you trying to access? ')
    return url


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
            'https://www.youtube.com/watch?v=SCE9XWg7RJU',
            download=False
        )
    manifest_url = yt_info
    return manifest_url


def trim_video_file(result):
    # trim video to 1 one frame
    stream = ffmpeg.input(result['url'])
    stream = stream.trim(start_frame=0, end_frame=1)
    base_path = os.path.dirname(__file__)
    print(base_path + 'recordings')
    path_of_video = os.path.abspath(os.path.join(base_path, 'recordings/{}.mp4'.format(datetime.now().microsecond)))
    stream = ffmpeg.output(stream, path_of_video)
    ffmpeg.run(stream)
    return base_path, path_of_video


def convert_video_to_image(paths):
    # convert mp4 to image
    vidcap = cv2.VideoCapture(paths[1])
    success, image = vidcap.read()
    count = 0
    success = True
    while success:
        cv2.imwrite(os.path.abspath(os.path.join(paths[0],
                                                 "images/frame%d.jpg" % count)),
                    image)  # save frame as JPEG file
        success, image = vidcap.read()
        count += 1


def retrieve_image_from_video_element(chrome):
    element = chrome.find_element_by_id("player-container")
    print(element)


if __name__ == '__main__':
    main()
