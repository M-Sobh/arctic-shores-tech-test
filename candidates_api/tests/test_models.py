from django.test import TestCase
from candidates_api.models import Candidate, Score

# Candidate Model #
################################
# candidate_ref must be a unique sequence of 8 digits and alphabets.


class CandidateTest(TestCase):
    def create_candidate(self, name='test', candidate_ref='34rt4r6y'):
        return Candidate.objects.create(name=name, candidate_ref=candidate_ref)

    def test_candidate_creation(self):
        w = self.create_candidate()
        self.assertTrue(isinstance(w, Candidate))
        self.assertEqual(w.__str__(), w.name)

############################
# Score Model #
############################
# score must be float between 0 - 100 inclusive.


# score must be stored in a list.
