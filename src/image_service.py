import os

import cv2


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


def get_dimensions_of_image(path_to_image):
    pass
