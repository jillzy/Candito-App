from django.urls import path
from . import views

urlpatterns = [
    path('', views.week_list, name='week_list'),
]