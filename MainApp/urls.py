from django.contrib import admin
from MainApp import views
from django.conf import settings
from django.urls import path

urlpatterns = [
    path('',views.uploadcsv,name = "uploadcsv"),
]
