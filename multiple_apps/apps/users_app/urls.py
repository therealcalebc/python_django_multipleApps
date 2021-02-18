from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
	# path('', views.index),
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('users/new', views.register, name='new'),
	path('users', views.list_users, name='list'),
]