from django.contrib import admin
from django.urls import path
from Assignment import views

urlpatterns = [
    path('', views.index, name = "Assignment"),
    # path('', views.uploadcsv, name='uploadcsv'),
    # path('', views.index, name = "data"),
]