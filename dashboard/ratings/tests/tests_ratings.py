from django.test import TestCase
from ratings.models import Rating
from ratings.tests.factories import RatingFactory

class RatingTestCase(TestCase):
    """Test basic Rating class behavior"""

    def test_create_rating(self):
        """You should be able to create a rating"""
        rating = RatingFactory()
        # There should be 1 rating
        self.assertEqual(1, Rating.objects.all().count())


    def test_update_rating(self):
        """You should be able to update rating values"""
        rating = RatingFactory(effort=10)
        self.assertEqual(10, Rating.objects.get(pk=1).effort)
        # Change effort value
        rating.effort = 5
        rating.save()
        # Should match the new value
        self.assertEqual(5, Rating.objects.get(pk=1).effort)


    def test_delete_rating(self):
        """You should be able to delete a rating"""
        rating = RatingFactory()
        # Should be 1 rating
        self.assertEqual(1, Rating.objects.all().count())
        # Delete it
        Rating.objects.get(pk=1).delete()
        # Should be no ratings
        self.assertEqual(0, Rating.objects.all().count())
