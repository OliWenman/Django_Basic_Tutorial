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

from .models import Choice, Question #, UploadFileForm
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

 		selected_choice = question.choice_set.get(pk = request.POST['choice'])


	except (KeyError, Choice.DoesNotExist):

		# Redisplay the question voting form
		return render(request, 
					  'Polls_App/detail.html',
					  {'question': question,
					   'error_message': "You didn't select a choice."})

	else:

		selected_choice.votes += 1
		question.no_votes += 1

		question.save()
		question.refresh_from_db()

		selected_choice.save()
		selected_choice.refresh_from_db()

		for choice in question.choice_set.all():

			choice.votes_percentage = (choice.votes/question.no_votes) * 100.
			choice.save()


		#Always return an HttpResponseRedirect after succesfully dealing
		#with POST data. This prevents data from being posted twice if
		#if a user hits the back button
		return HttpResponseRedirect(reverse('Polls_App:results', args=(question.id,)))

"""
def handle_uploaded_file(f):

	with open('some/file/name.txt', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)


def upload_file(request):
	
	if request.method == 'POST':
		form = UploadFileForm(request.Post, render.FILES)

		if form.is_valid():

			handle_upload_file(request.FILES['file'])
			return HttpResponseRedirect('/success/url')

		else:
			form = UploadFileForm()

		return render(request, 'upload.html', {'form': form})
"""
