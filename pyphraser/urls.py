from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderTemplate, name='render'),
    path('rephrase', views.rephrase)   
]

