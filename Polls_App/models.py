import datetime

from django.utils import timezone
from django.db import models
from django import forms

# Create your models here.
class Question(models.Model):

	question_text  = models.CharField(max_length=200)
	published_date = models.DateTimeField('date published')
	no_votes = models.IntegerField(default = 0)

	def __str__(self):
		return self.question_text

	def was_published_recently(self):

		now = timezone.now()
		return now - datetime.timedelta(days = 1) <= self.published_date <= now

	def reset_question_votes(self):
		no_votes = 0
		published_date = datetime.now()

	was_published_recently.admin_order_field = 'published_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):

	question = models.ForeignKey(Question, on_delete = models.CASCADE)

	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	votes_percentage = models.DecimalField(max_digits = 5, decimal_places=2, default=0.00)

	def __str__(self):
		return self.choice_text

"""
class UploadFileForm(forms.Form):

	title = forms.CharField(max_length=50)
	file  = forms.FileField()
 """

