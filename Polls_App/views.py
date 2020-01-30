"""
A view is a type of web page in your application that generally 
serves a specific functoon has a specific template.

Poll app
- Question "index" page, displays latest questions
- Question "detail" page, displays a question text, with
  no results but with a form to vote in.
- Question "results page", display results for a poll
- "Vote action - handles voting for  particular choice 
  in a particular question.
"""

#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404
#from django.http import Http404

from .models import Question

def index(request):

	latest_question_list = Question.objects.order_by('-published_date')[:5]

	#template = loader.get_template('Polls_App/index.html')

	context = {'latest_question_list': latest_question_list,}

	#output = ', '.join([q.question_text for q in latest_question_list])
	
	#return HttpResponse(template.render(context, request))

	return render(request, 'Polls_App/index.html', context)


def detail(request, question_id):
	"""
	try:
		question = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	"""

	question = get_object_or_404(Question, pk = question_id)
	#return HttpResponse("You're looking at question %s." % question_id)
	return render(request, 'Polls_App/detail.html', {'question' : question}) 

	


def	results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(repsonse % question_id)


def vote(request, question_id):
	return HttpResponse("Your're voting on question %s." % question_id)


