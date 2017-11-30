from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	template = 'profiles/home.html'
	return render(request, template, context)

def about(request):
	context = {}
	template = 'profiles/about.html'
	return render(request, template, context)