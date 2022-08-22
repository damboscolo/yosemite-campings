from django.http import HttpResponse
from yosemite.usecase import campsites_usecase
import json


def get_all_availabilities(request):
    start_date = request.GET['start_date']
    response = campsites_usecase.get_all_availabilities(start_date)
    return HttpResponse(response, status = 200)

def get_availabilities(request, id):
    start_date = request.GET['start_date']
    response = campsites_usecase.get_availabilities(id, start_date)
    return HttpResponse(response, status = 200)
