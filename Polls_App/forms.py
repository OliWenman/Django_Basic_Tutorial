from django import forms

class DocumentForms(forms.Form):

	docfile = forms.FileField(label = 'Selected a file',
							  hel_text = 'max. 42 megebytes')

	