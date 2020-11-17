from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
	path('get_upload_found_person_image_form', get_upload_found_person_image_form, name='get_upload_found_person_image_form'),
	path('upload_found_person_image_form', upload_found_person_image_form, name='upload_found_person_image_form'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 