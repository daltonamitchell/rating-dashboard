"""
Contains factory classes for quickly generating test data.

It uses the factory_boy package.

Please see https://github.com/rbarrois/factory_boy for more info
"""

import datetime
import factory
import random
from django.utils import timezone
from ratings import models

class SubmissionFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Submission
    application_date = timezone.now() - datetime.timedelta(days=random.randint(0, 5))
    submission_date = timezone.now() + datetime.timedelta(days=random.randint(1, 5))

class MediaFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Media
    filename = factory.Faker('file_name')
    filetype = factory.Faker('pystr', max_chars=200)
    submission = factory.SubFactory(SubmissionFactory)

class RatingFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Rating
    score = factory.Faker('pydecimal', left_digits=2, right_digits=1, positive=True)
    code_quality = factory.Faker('pyint')
    documentation = factory.Faker('pyint')
    problem_solving = factory.Faker('pyint')
    effort = factory.Faker('pyint')
    creativity = factory.Faker('pyint')
    originality = factory.Faker('pyint')
    submission = factory.SubFactory(SubmissionFactory)
