from django.urls import path
from . import views

urlpatterns = [
    path('', views.portal_analitico, name='portal_analitico'),
]