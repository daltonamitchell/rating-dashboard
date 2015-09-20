from math import sqrt

from django.shortcuts import render

from .models import Submission

from django.http import HttpResponse

def index(request):
    """Show all submissions"""
    # Set a default if ideals not passed in
    try:
        ideal_values = request.ideal_values
    except AttributeError:
        ideal_values = {
              'code_quality': 50,
              'documentation': 50,
              'problem_solving': 50,
              'effort': 50,
              'creativity': 100,
              'originality': 50,
        }
        pass

    top_submissions_list = Submission.objects.all()
    ranked_submissions_list = [_rank_submission(sub, ideal_values) for sub in top_submissions_list]
    context = {'top_submissions_list': ranked_submissions_list}
    return render(request, 'ratings/index.html', context)

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
        subtotal += (getattr(submission.rating, key) - ideal_values[key]) ** 2
    submission.rating.score = 1 / sqrt(subtotal)
    return submission
