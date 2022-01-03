from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CandidateSerializer, ScoreSerializer
from .models import Candidate, Score


# Endpoint /create-candidate
@api_view(['POST', ])
def api_create_candidate_view(request):
    if request.method == 'POST':
        candidate = Candidate.objects.get(pk=1)

        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Endpoint /get-candidate/{candidate_ref}

@api_view(['GET', ])
def api_get_candidate_by_ref(request, candidate_ref):
    try:
        candidate = Candidate.objects.get(candidate_ref=candidate_ref)
    except Candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)
