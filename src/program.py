import io

import cv2
import os
from datetime import datetime
import youtube_dl
import ffmpeg
from google.cloud import vision
from google.cloud.vision import types
import json
import pprint





from googleapiclient.discovery import build


def main():
    # ask user for URL
    # navigate pipto webpage
    # get html
    # parse html
    # retrieve image from yt video
    # post image to google cloud
    # config = get_config_info()
    # api_key = config["api_key"]
    # cse_id = config["cse_id"]
    # manifest_url = download_yt_video("https://www.youtube.com/watch?v=SCE9XWg7RJU")
    # path_of_video = trim_video_file(manifest_url)
    # path_of_image = convert_video_to_image(path_of_video)
    # text_from_image = detect_text(path_of_image)
    # results = google_search(text_from_image, api_key, cse_id, num=3)
    # for result in results:
    #     pprint.pprint(result)




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


def convert_video_to_image(paths):
    # convert mp4 to image
    vidcap = cv2.VideoCapture(paths[1])
    success, image = vidcap.read()
    success = True
    image_path = os.path.abspath(os.path.join(paths[0], "../images/frame-{}.jpg".format(datetime.today())))
    while success:
        cv2.imwrite(image_path, image)  # save frame as JPEG file
        success, image = vidcap.read()
    return image_path


def detect_text(path):
    """Detects text in the file."""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/usr/local/etc/Snatch-715850ed2d45.json"
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    # TO-DO: grab first element of text_annotations list
    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    print("first element: {}".format(texts[0].description))
    return texts[0].description


def choose_text_by_location(orientation, texts):
    if orientation is None:
        pass
    elif orientation == 'TOP_RIGHT':
        pass
    elif orientation == 'BOTTOM_LEFT':
        pass
    elif orientation == 'BOTTOM_RIGHT':
        pass
    elif orientation == 'TOP_LEFT':
        pass


def get_dimensions_of_image(path_to_image):
    pass


def google_search(search_term, api_key, cse_id, **kwargs):
    search_term = search_term.replace("\n", ' ')
    print("after replacement: {}".format(search_term))
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()

    # TODO: return "no_results" if there are none.

    return res['items']


def get_config_info():
    with open("./config/config.json") as config:
        data = json.load(config)

    return data


if __name__ == '__main__':
    main()
