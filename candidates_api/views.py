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
