from django import forms

from uploads.core.models import Document


class DocumentForm(forms.ModelForm):
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	class Meta:
		model = Document
		fields = ['title', 'description', 'document', ]