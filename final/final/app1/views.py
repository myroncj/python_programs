from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from app1.models import fucntion1
import matplotlib.pyplot as plt
import numpy as np

# Create your views here.

@csrf_exempt
def index(request):
	return render_to_response('index.html')


@csrf_exempt
def save1(request):
	f=float(request.POST['f'])
	a=int(request.POST['a'])
	b=int(request.POST['b'])
	n=int(request.POST['n'])

	h = (b-a)/float(n)
	s=0
	for i in range(1,n,1):
	    s += f*(a - (0.5*h) + i*h)
	ans1=h*s

	fun=fucntion1()
	fun.n=n
	fun.func=ans1
	fun.save()
	dict1={'answer': ans1}
	return render_to_response('answer.html',dict1)

@csrf_exempt
def save2(request):
	f=float(request.POST['f'])
	a=int(request.POST['a'])
	b=int(request.POST['b'])
	n=int(request.POST['n'])

	h = (b-a)/float(n)
	s=[]
	for i in range(1,n,1):
	    s.append(f*(a - (0.5*h) + i*h))
	sum2=sum(s)
	ans2=h*sum2

	fun=fucntion1()
	fun.n=n
	fun.func=ans2
	fun.save()
	dict1={'answer': ans2}
	return render_to_response('answer.html',dict1)

@csrf_exempt
def save3(request):
	f=float(request.POST['f'])
	a=int(request.POST['a'])
	b=int(request.POST['b'])
	n=int(request.POST['n'])

	h = (b-a)/float(n)
	s=[]
	for i in range(1,n,1):
	    s.append(f*(a - (0.5*h) + i*h))
	sum3=np.sum(s)
	ans3=h*sum3

	fun=fucntion1()
	fun.n=n
	fun.func=ans3
	fun.save()
	dict1={'answer':ans3}
	return render_to_response('answer.html',dict1)

@csrf_exempt
def display(request):
	list_n=fucntion1.objects.values_list('n',flat=True)
	list_fun=fucntion1.objects.values_list('func',flat=True)
	plt.plot(list_n,list_fun)
	plt.ylabel('midpoint rule')
	plt.xlabel('n')
	plt.show()
	return render_to_response('index.html')

@csrf_exempt
def write(request):
	list_n=fucntion1.objects.values_list('n',flat=True)
	list_fun=fucntion1.objects.values_list('func',flat=True)
	f = open("data1.txt", "w")
	for item in list_n:
		f.write("%s\n" % item)
	for item in list_fun:
		f.write("%s\n" % item)
	return render_to_response('index.html')