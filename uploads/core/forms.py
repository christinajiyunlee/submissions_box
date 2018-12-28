from django import forms
from uploads.core.models import Document


class DocumentForm(forms.ModelForm):
	
	class Meta:
		model = Document
		fields = ['title', 'description', 'file_1', 'file_2', 'file_3', 'file_4', 'file_5']
