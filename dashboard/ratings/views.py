from math import sqrt

from django.shortcuts import render, redirect

from ratings.models import Submission


def index(request):
    """Show all submissions"""
    # Set a default if ideals not passed in
    if request.method == 'POST' and 'ideal_values' in request.POST:
        import json
        ideal_values = json.loads(request.POST.get('ideal_values'))
    else:
        ideal_values = {
              'code_quality': 5,
              'documentation': 5,
              'problem_solving': 5,
              'effort': 5,
              'creativity': 5,
              'originality': 5,
        }

    top_submissions_list = Submission.objects.all()
    ranked_submissions_list = [_rank_submission(sub, ideal_values) for sub in top_submissions_list]
    context = {'top_submissions_list': ranked_submissions_list}
    return render(request, 'ratings/index.html', context)

def create(request):
    """Show the form for creating new submissions"""
    return render(request, 'ratings/new.html', {})

def store(request):
    """Save a new submission"""
    from ratings.tests.factories import SubmissionFactory, MediaFactory, RatingFactory

    if request.method == 'POST':
        submission = SubmissionFactory()
        MediaFactory(submission=submission)
        RatingFactory(score=0,
                      code_quality=request.POST.get('code_quality'),
                      documentation=request.POST.get('documentation'),
                      problem_solving=request.POST.get('problem_solving'),
                      effort=request.POST.get('effort'),
                      creativity=request.POST.get('creativity'),
                      originality=request.POST.get('originality'),
                      submission=submission)

    return redirect('index')

def _rank_submission(submission, ideal_values):
    """Ranks a submission by ideal values

    Args:
        submission (Submission): The submission object to be ranked.
        ideal_values (dict): Ideal values used to rank the submission.

    Returns:
        (Submission): Returns the submission object with score set to the new
                      ranking value.
    """
    subtotal = 0
    for key in ideal_values:
        subtotal += (getattr(submission.rating, key) * (ideal_values[key] / 10)) ** 2
    submission.rating.score = sqrt(subtotal)
    return submission
