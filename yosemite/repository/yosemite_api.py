from tokenize import group
import requests
import json
import os

ENV = os.environ.get('ENV')

def get_availabilities(campground_id, start_date):
    if ENV != "prod": return _mock_get_availabilities()

    url = "https://www.recreation.gov/api/camps/availability/campground/{0}/month?start_date={1}T00%3A00%3A00.000Z".format(campground_id, start_date)
    headers = {
        "authority": "www.recreation.gov",
        "referer": "https://www.recreation.gov/camping/campgrounds/232449",
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        }
    return requests.get(url, headers=headers).json()

def _mock_get_availabilities():
    f = open("yosemite/repository/availabilities_mock.json")
    data = json.load(f)
    f.close()
    return data
