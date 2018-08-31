from django.shortcuts import render
from .models import Resources, Questions, Events, Placement, Projects

# Create your views here.

def index(request):
	resources = Resources.objects.all
	return render(request,'MEA/index.html', {'resources':resources})

def placements(request):
	return render(request, 'MEA/placements.html',{})

def events(request):
	ev = Events.objects.all
	return render(request, 'MEA/events.html',{'events' : ev})

def tests(request):
	return render(request, 'MEA/tests.html',{})

def projects(request):
	proj = Projects.objects.all
	return render(request, 'MEA/projects.html', {'projects' : proj})

def specprojects(request,name1):
	proj = Projects.objects.filter(name=name1)
	return render(request, 'MEA/specprojects.html', {'projects' : proj[0]})

def specevents(request,name1):
	eve = Events.objects.filter(name=name1)
	return render(request, 'MEA/specevents.html', {'events' : eve[0]})

	