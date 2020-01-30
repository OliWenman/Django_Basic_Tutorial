from django.urls import path
from . import views

app_name = 'Polls_App'
urlpatterns = [
	# ex: /Polls_App/
	path('', views.index, name = 'index'),

	# ex: /Polls_App/5/
	path('<int:question_id>/', views.detail, name = 'detail'),

	# ex: /Polls_App/5/results/
	path('<int:question_id>/results/', views.results, name = 'results'),

	# ex: /Polls_App/5/vote/
	path('<int:question_id>/vote/', views.vote, name = 'vote'),
]

