from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return redirect('/users')

def register(request):
	# return HttpResponse("placeholder for users to create a new user record")
	context = {
		'title': "Users App",
		'message': "placeholder for users to create a new user record"
	}
	return render(request, 'users.index.html', context)

def login(request):
	# return HttpResponse("placeholder for users to log in")
	context = {
		'title': "Users App",
		'message': "placeholder for users to log in"
	}
	return render(request, 'users.index.html', context)

def list_users(request):
	# return HttpResponse("placeholder to later display all the list of users")
	context = {
		'title': "Users App",
		'message': "placeholder to later display all the list of users"
	}
	return render(request, 'users.index.html', context)