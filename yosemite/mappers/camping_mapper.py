from datetime import datetime

def response_to_model(id, campsite, date, status):
    return {
        "campsite_id": id,
        "campsite_type": campsite['campsite_type'],
        "site": campsite['site'],
        "name": campsite['loop'],
        "date": datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z"),
        "status": status
    }