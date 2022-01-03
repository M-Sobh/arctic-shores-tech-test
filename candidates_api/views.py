from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def create_candidate(request):
    message = f'New Candidate Created'
    return HttpResponse(message)
