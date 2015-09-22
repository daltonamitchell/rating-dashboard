"""
Seeds the database with Faker data for testing.

Usage:
    from ratings.tests.seeder import Seeder
    ...
    Seeder.seed()

    Enjoy your new data!
"""

from ratings.tests.factories import *

class Seeder(object):
    @staticmethod
    def seed():
        """Populate database with seed data"""
        for i in range(10):
            sub = SubmissionFactory()
            MediaFactory.create_batch(2, submission=sub)
            RatingFactory(submission=sub)
        return 'Seeding complete.'
