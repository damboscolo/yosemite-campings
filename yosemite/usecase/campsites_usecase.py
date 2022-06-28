from yosemite.repository import yosemite_api

def get_campings(campground_id):
    campsites = yosemite_api.get_campings(campground_id)['campsites']

    all = []
    for campsite_id in campsites.keys():
        availabilities = campsites[campsite_id]['availabilities']

        for date in availabilities.keys():
            all += [parse(campsite_id, campsites[campsite_id], date, availabilities[date])]

    not_reserved = list(filter(lambda campsites: campsites['status'] == 'Available', all))
    print(not_reserved)

    return not_reserved

def parse(id, campsite, date, status):
    return {
        "campsite_id": id,
        "campsite_type": campsite['campsite_type'],
        "site": campsite['site'],
        "date": date,
        "status": status
    }
    