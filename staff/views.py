from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse
# Create your views here.

operations={
    "view": "view.html",
    "ping":"ping.html",
    "profile": "profile.html",
    "overtime": "overtime.html",
}

def Operation(request, operation):
    try:
        return  render(request,operations[operation])
    except:
        return HttpResponse(HttpResponseNotFound("Nereye geldin!"))