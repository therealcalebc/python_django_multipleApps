from django.shortcuts import render, redirect, HttpResponse

def index(request):
	# return HttpResponse("placeholder to later display a list of all the surveys created")
	context = {
		'title': "Surveys App",
		'message': "placeholder to later display a list of all the surveys created"
	}
	return render(request, 'surveys.index.html', context)

def new(request):
	# return HttpResponse("placeholder for users to add a new survey")
	context = {
		'title': "Surveys App",
		'message': "placeholder for users to add a new survey"
	}
	return render(request, 'surveys.index.html', context)