"""
Contains factory classes for quickly generating test data.

It uses the factory_boy package.

Please see https://github.com/rbarrois/factory_boy for more info
"""

import datetime
import factory
import factory.fuzzy
import random
from django.utils import timezone
from ratings import models

class SubmissionFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Submission
    application_date = factory.fuzzy.FuzzyDateTime(timezone.now(), timezone.now() + datetime.timedelta(days=30))
    submission_date = factory.fuzzy.FuzzyDateTime(timezone.now(), timezone.now() + datetime.timedelta(days=100))

class MediaFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Media
    filename = factory.Faker('file_name')
    filetype = factory.Faker('pystr', max_chars=60)
    submission = factory.SubFactory(SubmissionFactory)

class RatingFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Rating
    score = factory.Faker('pydecimal', left_digits=2, right_digits=1, positive=True)
    code_quality = factory.fuzzy.FuzzyInteger(0,100)
    documentation = factory.fuzzy.FuzzyInteger(0,100)
    problem_solving = factory.fuzzy.FuzzyInteger(0,100)
    effort = factory.fuzzy.FuzzyInteger(0,100)
    creativity = factory.fuzzy.FuzzyInteger(0,100)
    originality = factory.fuzzy.FuzzyInteger(0,100)
    submission = factory.SubFactory(SubmissionFactory)
