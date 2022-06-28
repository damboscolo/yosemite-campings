from django.http import HttpResponse
from yosemite.usecase import campsites_usecase
import json

def get_campings(request, id):
    response = campsites_usecase.get_campings(id)
    return HttpResponse(response, status = 200)