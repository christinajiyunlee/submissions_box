from __future__ import unicode_literals

from django.db import models
from django import forms

class Document(models.Model):
	title = models.CharField(max_length=30, blank=True)
	description = models.CharField(max_length=255, blank=True)
	file_1 = models.FileField(upload_to='documents/', blank=True)
	file_2 = models.FileField(upload_to='documents/', blank=True)
	file_3 = models.FileField(upload_to='documents/', blank=True)
	file_4 = models.FileField(upload_to='documents/', blank=True)
	file_5 = models.FileField(upload_to='documents/', blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)
    # User automatically collected