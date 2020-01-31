from django.urls import path
from . import views

app_name = 'Polls_App'
urlpatterns = [
	# ex: /Polls_App/
	path('', views.IndexView.as_view(), name = 'index'),

	# ex: /Polls_App/5/
	path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),

	# ex: /Polls_App/5/results/
	path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),

	# ex: /Polls_App/5/vote/
	path('<int:question_id>/vote/', views.vote, name = 'vote'),
]

