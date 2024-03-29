from yosemite.repository import yosemite_api, telegram
from yosemite.mappers import camping_mapper
import os
import json
import datetime

CAMPSITE_IDS = json.loads(os.environ.get('CAMPSITE_IDS', []))

def get_all_availabilities(start_date):
    response = []
    for id in CAMPSITE_IDS:
        response += [get_availabilities(id, start_date)]
    return response


def get_availabilities(campground_id, start_date):
    campsites = yosemite_api.get_availabilities(campground_id, start_date)['campsites']

    all = []
    for campsite_id in campsites.keys():
        availabilities = campsites[campsite_id]['availabilities']

        for date in availabilities.keys():
            camping_model = camping_mapper.response_to_model(campsite_id, campsites[campsite_id], date, availabilities[date])
            # if camping_model['date'].date() >= datetime.date(2022, 7, 15) and camping_model['date'].date() <= datetime.date(2022, 7, 15):
            all += [camping_model]

    not_reserved = list(filter(lambda campsites: campsites['status'] == 'Available', all))

    message = _format_telegram_message(not_reserved, campground_id, start_date)
    if len(not_reserved) > 0:
        telegram.send_message(message)

    return message


def _format_telegram_message(campings, id, start_date):
    if len(campings) == 0: return "There is no availability for camping %s for date higher than %s!" % (id, start_date)

    text = "⭐ *Available campsites for %s * ⭐\n\n" %  id
    for c in campings:
        text += "*%s* %s *site:* %s - %s\n" % (c['name'], c['date'], c['site'], c['campsite_type'])
    return text
