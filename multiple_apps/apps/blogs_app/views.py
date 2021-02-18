from django.shortcuts import render, redirect, HttpResponse

def index(request):
	# return HttpResponse("placeholder to later display a list of all blogs")
	context = {
		'title': "Blogs App",
		'message': "placeholder to later display a list of all blogs"
	}
	return render(request, 'blogs.index.html', context)

def new(request):
	# return HttpResponse("placeholder to display a new form to create a new blog")
	context = {
		'title': "Blogs App",
		'message': "placeholder to display a new form to create a new blog"
	}
	return render(request, 'blogs.index.html', context)

def create(request):
	return redirect('/blogs')

def show(request, number):
	# return HttpResponse(f"placeholder to display blog number: {number}")
	context = {
		'title': "Blogs App",
		'message': f"placeholder to display blog number: {number}"
	}
	return render(request, 'blogs.index.html', context)

def edit(request, number):
	# return HttpResponse(f"placeholder to edit blog number: {number}")
	context = {
		'title': "Blogs App",
		'message': f"placeholder to edit blog number: {number}"
	}
	return render(request, 'blogs.index.html', context)

def destroy(request, number):
	return redirect('/blogs')