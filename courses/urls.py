from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcoming_courses, name='upcoming_courses'),
]

