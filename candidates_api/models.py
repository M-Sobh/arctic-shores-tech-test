from django.db import models

# Create your models here.


class Candidate(models.Model):
    name = models.CharField(max_length=60)
    candidate_ref = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Score(models.Model):
    score = models.FloatField(max_length=3)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __float__(self):
        return self.score
