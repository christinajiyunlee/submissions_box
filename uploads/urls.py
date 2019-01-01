# Every additioanl page you wish to add should be added to urlpatterns
# Read more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from uploads.core import views

urlpatterns = [
	path('', views.home, name='home'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
