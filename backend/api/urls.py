from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
    path('add', views.api_add)
]