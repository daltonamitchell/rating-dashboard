from django.shortcuts import render

from .models import Submission

from django.http import HttpResponse

def index(request):
    """Show all submissions"""
    top_submissions_list = Submission.objects.all()
    context = {'top_submissions_list': top_submissions_list}
    return render(request, 'ratings/index.html', context)
