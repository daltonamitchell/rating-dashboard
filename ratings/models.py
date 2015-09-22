import uuid
from django.db import models


class Submission(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    application_date = models.DateTimeField()
    submission_date = models.DateTimeField()
    def __str__(self):
        uid = self.uuid.urn
        return uid[9:]


class Media(models.Model):
    filename = models.TextField()
    filetype = models.CharField(max_length=200)
    submission = models.ForeignKey(Submission)
    def __str__(self):
        return self.filename


class Rating(models.Model):
    score = models.DecimalField(default=0,max_digits=5,decimal_places=2)
    code_quality = models.IntegerField(default=0)
    documentation = models.IntegerField(default=0)
    problem_solving = models.IntegerField(default=0)
    effort = models.IntegerField(default=0)
    creativity = models.IntegerField(default=0)
    originality = models.IntegerField(default=0)
    submission = models.OneToOneField(Submission)
    def __str__(self):
        return self.submission.uuid.urn[9:] + ": " + str(self.score)
