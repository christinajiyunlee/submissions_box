# Define how you will store data (model fields)
# Read more here: https://docs.djangoproject.com/en/2.1/topics/db/models/

from __future__ import unicode_literals

from django.db import models
from django import forms

# Document accepts up to 5 files. User can submit form with less than 5 files.
class Document(models.Model):
	title = models.CharField(max_length=30, blank=True)
	description = models.CharField(max_length=255, blank=True)
	file_1 = models.FileField(upload_to='documents/', blank=True) # Default value is blank when page is first loaded
	file_2 = models.FileField(upload_to='documents/', blank=True) # All uploaded files currently are routed to the 'documents' folder in the same directory
	file_3 = models.FileField(upload_to='documents/', blank=True)
	file_4 = models.FileField(upload_to='documents/', blank=True)
	file_5 = models.FileField(upload_to='documents/', blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True) # Currently stores time stamps in GMT
    # Uploader collected from log in account

class DocumentForm(forms.ModelForm):
	class Meta:
		# Adding meta data, that are not fields. Read more here: https://docs.djangoproject.com/en/dev/topics/db/models/#meta-options
		model = Document # Assign document model to 
		fields = ['title', 'description', 'file_1', 'file_2', 'file_3', 'file_4', 'file_5']