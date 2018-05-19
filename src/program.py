import pprint
from search_service import google_search, get_config_info
from video_service import download_yt_video, trim_video_file
from image_service import convert_video_to_image
from text_service import detect_text


def main():

    # ask user for URL
    # navigate pipto webpage
    # get html
    # parse html
    # retrieve image from yt video
    # post image to google cloud
    config = get_config_info()
    api_key = config["api_key"]
    cse_id = config["cse_id"]
    manifest_url = download_yt_video("https://www.youtube.com/watch?v=SCE9XWg7RJU")
    path_of_video = trim_video_file(manifest_url)
    path_of_image = convert_video_to_image(path_of_video)
    text_from_image = detect_text(path_of_image)
    results = google_search(text_from_image, api_key, cse_id, num=3)
    for result in results:
        pprint.pprint(result)


if __name__ == '__main__':
    main()
