# This is where you define the python function (home(request)) that accepts a web request and returns a HTML page

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import DocumentForm

def home(request):
    if request.method == 'POST': 
        form = DocumentForm(request.POST, request.FILES) # Instantiating DocumentForm object
        if form.is_valid():
            _new = form.save(commit=False)
            _new.save()
            form.save_m2m()
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', { 'form': form })