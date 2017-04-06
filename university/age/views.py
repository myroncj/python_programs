from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from age.models import Student1

@csrf_exempt
def index(request):
	return render_to_response('index.html')

@csrf_exempt
def save(request):
	name=request.GET['nm']
	age=request.GET['ag']
	s=Student1()
	s.name=name
	s.age=age
	s.save()
	view(request)
	return render_to_response('save.html')

@csrf_exempt
def view(request):
	sum=0
	for i in Student1.objects.all():
		sum+=i.age
	print(sum)
