import io
import os

from google.cloud import vision
from google.cloud.vision import types


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
