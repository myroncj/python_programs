from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''def display_name(request):
	return HttpResponse("Fodela re? -_- ")
'''

def display_name(request):
	name="MyronCJ"
	return HttpResponse("My name is "+name)

def pass_variable(request):
	x = request.GET['a']
	return HttpResponse("Variable is "+x)