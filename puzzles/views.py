from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Player, Submission
from django.shortcuts import get_object_or_404
from django.db.models import Count, Case, When, IntegerField, Sum

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'puzzles/index.html', context)
	
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'puzzles/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def submission(request, question_id):
	return HttpResponse("You're submitting for question %s." % question_id)
	
def leaderboard(request):
	result = Submission.objects.values_list('player_id')	
	return render(request, 'puzzles/leaderboard.html', locals())
