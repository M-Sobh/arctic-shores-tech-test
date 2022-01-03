from django.db.models import fields
from rest_framework import serializers
from .models import Candidate, Score


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name', 'candidate_ref')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('score')
