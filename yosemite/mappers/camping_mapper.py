
def response_to_model(id, campsite, date, status):
    return {
        "campsite_id": id,
        "campsite_type": campsite['campsite_type'],
        "site": campsite['site'],
        "date": date,
        "status": status
    }