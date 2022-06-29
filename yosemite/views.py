from django.http import HttpResponse
from yosemite.usecase import campsites_usecase
import json


def get_all_availabilities(request):
    response = campsites_usecase.get_all_availabilities()
    return HttpResponse(response, status = 200)

def get_availabilities(request, id):
    response = campsites_usecase.get_availabilities(id)
    return HttpResponse(response, status = 200)
