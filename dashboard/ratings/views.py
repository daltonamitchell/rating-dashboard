from math import sqrt

from django.shortcuts import render

from .models import Submission

from django.http import HttpResponse

def index(request):
    """Show all submissions"""
    # Set a default if ideals not passed in
    if request.method == 'POST' and 'ideal_values' in request.POST:
        import ast
        ideal_values = ast.literal_eval(request.POST.get('ideal_values')) # Convert string to dict
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
