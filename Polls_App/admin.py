from django.contrib import admin
from .models import Question, Choice
#from .models import Test

# Register your models here.
#admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3
	n_votes = Choice.votes

class QuestionAdmin(admin.ModelAdmin):

	list_filter = ['published_date']
	search_filter = ['question_text']

	list_display = ('question_text', 
					'published_date', 
					'was_published_recently',)

	fieldsets = [(None, {'fields': ['question_text']}),
				 ('Date information', {'fields': ['published_date'], 'classes': ['collapse']})]

	inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Test)
