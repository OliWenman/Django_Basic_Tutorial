from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3
	fields = ('question', 'choice_text')

class QuestionAdmin(admin.ModelAdmin):

	list_filter = ['published_date']
	search_filter = ['question_text']

	list_display = ('question_text',
					'no_votes', 
					'published_date', 
					'was_published_recently')

	fieldsets = [(None, {'fields': ['question_text']}),
				 ('Date information', {'fields': ['published_date'], 'classes': ['collapse']})]

	inlines = [ChoiceInLine]

	def reset_action(self, obj):

		return format_html('<a class="button" href="{}">Reset</a>',
						    reverse('admin:question', args=[obj.pk]),)


admin.site.register(Question, QuestionAdmin)
