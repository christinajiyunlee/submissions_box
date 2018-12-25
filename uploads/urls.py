# from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from uploads.core import views

urlpatterns = [
	path('', views.home, name='home'),
    path('uploads/simple/', views.simple_upload, name='simple_upload'),
    path('uploads/form/', views.model_form_upload, name='model_form_upload'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
