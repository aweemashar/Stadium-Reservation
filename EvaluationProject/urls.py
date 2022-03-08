from django.urls import path
from django.contrib import admin
from EvaluationAPI.views import *
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^manage', manage_view),
    url(r'^create_restaurant', create_restaurant),
    url(r'^get_restaurant', get_restaurant),
    url(r'^get_stadium_free_time_slot', get_stadium_free_time_slot),


]
