from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
	path('get_upload_lost_person_image_form', get_upload_lost_person_image_form, name='get_upload_lost_person_image_form'),
	path('upload_lost_person_details', upload_lost_person_details, name='upload_lost_person_details'),
	path('submit_another', submit_another, name='submit_another')
]