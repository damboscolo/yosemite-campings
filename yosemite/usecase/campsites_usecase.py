from yosemite.repository import yosemite_api, telegram
from yosemite.mappers import camping_mapper
import os
import json

CAMPSITE_IDS = json.loads(os.environ.get('CAMPSITE_IDS', []))

def get_all_availabilities():
    response = []
    for id in CAMPSITE_IDS:
        response += [get_availabilities(id)]
    return response


def get_availabilities(campground_id):
    campsites = yosemite_api.get_availabilities(campground_id)['campsites']

    all = []
    for campsite_id in campsites.keys():
        availabilities = campsites[campsite_id]['availabilities']

        for date in availabilities.keys():
            all += [camping_mapper.response_to_model(campsite_id, campsites[campsite_id], date, availabilities[date])]

    not_reserved = list(filter(lambda campsites: campsites['status'] == 'Available', all))
   
    message = _format_telegram_message(not_reserved, campground_id)
    telegram.send_message(message)
    print(message)

    return message


def _format_telegram_message(campings, id):
    if len(campings) == 0: return "There is no availability for camping %s for July!" % id
    
    text = "⭐ *Available campsites for %s * ⭐\n\n" %  id
    for c in campings:
        text += "%s *site:* %s - *%s*\n" % (c['date'], c['site'], c['campsite_type'])
    return text