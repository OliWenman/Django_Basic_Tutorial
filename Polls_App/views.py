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

from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from django.shortcuts import render, get_object_or_404
#from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone

class IndexView(generic.ListView):

	template_name = 'Polls_App/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):

		"""
		Return the last five published questions.
		"""
		return Question.objects.filter(published_date__lte = timezone.now()).order_by('published_date')[:5]

class DetailView(generic.DetailView):

	model = Question
	template_name = 'Polls_App/detail.html'

	def get_queryset(self):

		"""
		Excludes any questions that aren't published yet
		"""

		return Question.objects.filter(published_date__lte = timezone.now())


class ResultsView(generic.DetailView):

	model = Question
	template_name = 'Polls_App/results.html'
	


def vote(request, question_id):

	question = get_object_or_404(Question, pk = question_id)

	try:

		#if request.method=="POST":

 		#	choice = request.POST.get('choice', None)
 		#	if choice is not None:

 		#		selected_choice = question.choice_set.get(pk=choice)
 		selected_choice = question.choice_set.get(pk = request.POST['choice'])


	except (KeyError, Choice.DoesNotExist):

		# Redisplay the question voting form
		return render(request, 
					  'Polls_App/detail.html',
					  {'question': question,
					   'error_message': "You didn't select a choice."})

	else:
		selected_choice.votes += 1
		selected_choice.save()
		selected_choice.refresh_from_db()

		#Always return an HttpResponseRedirect after succesfully dealing
		#with POST data. This prevents data from being posted twice if
		#if a user hits the back button
		return HttpResponseRedirect(reverse('Polls_App:results', args=(question.id,)))

	


