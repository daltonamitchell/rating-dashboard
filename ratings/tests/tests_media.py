from django.test import TestCase
from ratings.models import Media
from ratings.tests.factories import MediaFactory

class MediaTestCase(TestCase):
    """Test basic Media class behavior"""

    def test_create_media(self):
        """You should be able to create a Media record"""
        # Create a Media object & associated Submission
        MediaFactory()
        # There should be 1 Media record
        self.assertEqual(1, Media.objects.all().count())


    def test_update_media(self):
        """You should be able to update a Media records values"""
        media = MediaFactory()
        # Edit & save
        media.filetype = 'Web Application'
        media.save()
        # Record should reflect the change
        self.assertEqual('Web Application', Media.objects.get(pk=1).filetype)


    def test_delete_media(self):
        """You should be able to delete a Media record"""
        MediaFactory()
        # Should have 1 Media record
        self.assertEqual(1, Media.objects.all().count())
        # Delete it
        Media.objects.get(pk=1).delete()
        # Should have 0 Media records
        self.assertEqual(0, Media.objects.all().count())
