from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def create_candidate(request):
    message = f'New Candidate Created'
    return HttpResponse(message)


def create_score(request):
    message = f'New Score Added'
    return HttpResponse(message)


def get_candidate_by_ref(request, candidate_ref):
    message = f'Candidate of reference {candidate_ref} successfully hooked'
    return HttpResponse(message)
