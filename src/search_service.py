import json
from googleapiclient.discovery import build


def get_config_info():
    with open("./config/config.json") as config:
        data = json.load(config)

    return data


def google_search(search_term, api_key, cse_id, **kwargs):
    search_term = search_term.replace("\n", ' ')
    print("after replacement: {}".format(search_term))
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()

    # TODO: return "no_results" if there are none.

    return res['items']