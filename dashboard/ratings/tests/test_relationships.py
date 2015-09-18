from django.test import TestCase
from ratings.models import Submission, Media, Rating
from ratings.tests.factories import SubmissionFactory, MediaFactory, RatingFactory

class RelationshipTestCase(TestCase):
    """Test basic model relationship behavior"""

    def test_submission_can_lookup_relationships(self):
        """A Submission should be able to query it's Rating & Media records"""
        # Create one of each model and associate them
        submission = SubmissionFactory()
        media = MediaFactory(submission=submission)
        rating = RatingFactory(submission=submission)
        # Submission should have a Media object
        self.assertIs( type(submission.media_set.all()[0]), Media )
        # Submission should have a Rating object
        self.assertIs( type(submission.rating), Rating )
        # They should be the objects created above
        self.assertEqual( submission.media_set.all()[0], media )
        self.assertEqual( submission.rating, rating )
