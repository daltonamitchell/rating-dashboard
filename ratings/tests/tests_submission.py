import datetime
from django.test import TestCase
from django.utils import timezone
from ratings.models import Submission

class SubmissionTestCase(TestCase):
    """Test basic Submission class behavior"""

    def test_create_submission(self):
        """You should be able to add a new submission to the db"""
        submission = Submission.objects.create(application_date=timezone.now(),
                                                submission_date=timezone.now() + datetime.timedelta(days=2))
        # There should be 1 Submission
        self.assertEqual(1, Submission.objects.all().count())
        # UUID's should match
        self.assertEqual(submission.uuid, Submission.objects.get(pk=1).uuid)

    def test_update_submission(self):
        """You should be able to update a submissions values"""
        submission = Submission.objects.create(application_date=timezone.now(),
                                                submission_date=timezone.now() + datetime.timedelta(days=2))
        # Dates should match
        self.assertEqual(submission.submission_date, Submission.objects.get(pk=1).submission_date)
        # Change date
        submission.submission_date = timezone.now() + datetime.timedelta(days=35)
        submission.save()
        # Dates should still match
        self.assertEqual(submission.submission_date, Submission.objects.get(pk=1).submission_date)

    def test_delete_submission(self):
        """You should be able to delete a submission"""
        submission = Submission.objects.create(application_date=timezone.now(),
                                                submission_date=timezone.now() + datetime.timedelta(days=2))
        # There should be 1 submission
        self.assertEqual(1, Submission.objects.all().count())
        # Delete it
        Submission.objects.get(pk=1).delete()
        # There should be no submissions
        self.assertEqual(0, Submission.objects.all().count())
