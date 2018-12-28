from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm


def home(request):
    documents = Document.objects.all()

    return render(request, 'core/home.html', { 'documents': documents })

#-----------------------
def model_form_upload(request):

    # documents = Document.objects.all()

    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            _new = form.save(commit=False)
            _new.save()
            form.save_m2m()
        return redirect('model_form_upload')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', { 'form': form })
#-----------------------

# NOT RELEVANT ONE
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


