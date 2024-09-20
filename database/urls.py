from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #path('database', views.viewDatabase, name="database"),
]
