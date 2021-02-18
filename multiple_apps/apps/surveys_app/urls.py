from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns = [
	path('', views.index, name='index'),
	path('new', views.new, name='new'),
]