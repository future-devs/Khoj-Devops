from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
	path('get_analysis', get_analysis, name='get_analysis'),
	path('police_dashboard', police_dashboard, name='police_dashboard'),
	path('get_upload_lost_person_image_form', get_upload_lost_person_image_form, name='get_upload_lost_person_image_form'),
	path('get_upload_found_person_image_form', get_upload_found_person_image_form, name='get_upload_found_person_image_form'),
	path('get_heatmap', display_heatmap, name='get_heatmap')
]