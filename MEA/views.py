from django.shortcuts import render
from .models import Resources, Questions, Events, Placement, Projects

# Create your views here.

def index(request):
	resources = Resources.objects.all
	return render(request,'MEA/index.html', {'resources':resources})

def placements(request):
	place = Placement.objects.all
	return render(request, 'MEA/placements.html',{'placements':place})

def events(request):
	ev = Events.objects.all
	return render(request, 'MEA/events.html',{'events' : ev})

def tests(request):
	return render(request, 'MEA/tests.html',{})

def projects(request):
	proj = Projects.objects.all
	return render(request, 'MEA/projects.html', {'projects' : proj})

def specprojects(request,name1):
	allproj = Projects.objects.all
	proj = Projects.objects.filter(name=name1)
	return render(request, 'MEA/specprojects.html', {'projects' : proj[0],'allproj':allproj})

def specevents(request,name1):
	allev = Events.objects.all
	eve = Events.objects.filter(name=name1)
	return render(request, 'MEA/specevents.html', {'events' : eve[0],'allev':allev})

def specplacements(request,name1,comp):
	allplace = Placement.objects.all
	specplace = Placement.objects.filter(name=name1,company=comp)
	return render(request, 'MEA/specplacements.html', {'specplace' : specplace[0],'allplace':allplace})

def spectests(request,cat):
	ques = Questions.objects.filter(category=cat).order_by('?')[:2]
	ansmarked =[]
	return render(request, 'MEA/spectests.html', {'questions' : ques,'ansmarked':ansmarked})

def check(request):
	if  request.method == 'POST':
		selected =[]
		quesid =[]
		score =0;
		for x in range(0,2):
			stir='ans'+str(x)
			que='existq'+str(x)
			ch = request.POST[stir]
			selected.append(ch)
			qid = request.POST[que]
			quesid.append(qid)
		print(quesid)
		for idd,x in enumerate(quesid):
			qu=Questions.objects.filter(id=x)
			if(qu[0].correct == selected[idd]):
				score+=1
		qio =Questions.objects.filter(id__in=quesid)
		qs = zip(qio,selected)
		return render(request, 'MEA/check.html', {'score':score,'qs' : qs})
		# for x in range(0,2):
		# 	if(questions[x].correct == ch):
		# 		print('Correct')





	