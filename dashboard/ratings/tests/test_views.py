from django.test import TestCase, Client

from ratings.models import Rating

from ratings.tests.factories import SubmissionFactory, MediaFactory, RatingFactory
from ratings.tests.helpers import RatingValues


class IndexViewTestCase(TestCase):
    def test_index_view_with_no_submissions(self):
        """
        If no submissions exist, an appropriate message should be displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There aren't any submissions yet.")
        self.assertQuerysetEqual(response.context['top_submissions_list'], [])

    def test_index_view_with_a_submission(self):
        """
        If a submission has been created, it should be displayed
        """
        submission = SubmissionFactory()
        RatingFactory(submission=submission)
        MediaFactory(submission=submission)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Submission #{}'.format(submission.id))
        self.assertQuerysetEqual(response.context['top_submissions_list'], ['<Submission: ' + str(submission) + '>'])

    def test_index_view_with_ideal_values(self):
        """
        If I pass in ideal_values the submissions should be score accorind to
        those values
        """
        # Set and ideal value preferring code quality
        ideal = {
            'code_quality': 10,
            'documentation': 5,
            'problem_solving': 5,
            'effort': 5,
            'creativity': 5,
            'originality': 5,
        }

        # Create ratings preferring code quality
        code_sub = SubmissionFactory()
        MediaFactory(submission=code_sub)
        RatingFactory(submission=code_sub, **RatingValues.prefer_code())

        # Create ratings preferring different attributes
        r2 = RatingFactory(**RatingValues.prefer_problem_solving())
        MediaFactory(submission=r2.submission)

        r3 = RatingFactory(**RatingValues.prefer_effort())
        MediaFactory(submission=r3.submission)

        r4 = RatingFactory(**RatingValues.prefer_creativity())
        MediaFactory(submission=r4.submission)

        # Bring up index to get top submissions list
        response = self.client.get('/', {'ideal_values': ideal})

        # Sort ratings by score
        submissions = response.context['top_submissions_list']
        sorted_submissions = sorted(submissions, key=lambda sub: sub.rating.score)

        # The highest code quality should have the highest score
        self.assertEqual(sorted_submissions[-1], code_sub)
