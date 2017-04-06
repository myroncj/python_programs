from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from chips.models import chips1
from chips.models import gps
import matplotlib.pyplot as plt
import numpy as np
import math

# Create your views here.

@csrf_exempt
def index(request):
	return render_to_response('index.html')

@csrf_exempt
def save(request):
	t=request.GET['t']
	s=request.GET['s']
	c=chips1()
	c.t=t
	c.s=s
	c.save()
	return render_to_response('save.html')
            
'''@csrf_exempt
def save(request):
  a=float(request.POST['a'])
  u=float(request.POST['u'])
  t=10;
  slist=[]
  tlist=[]
  s=0
  obj=Values()
  while t<30:
    s=(u*t)+(0.5*a*t*t)
    obj.s=s
    obj.t=t
    obj.save()
    slist.append(s)
    tlist.append(t)
    t+=2
  plt.plot(slist,tlist)
  plt.show()
  return render_to_response("index.html");'''

#Practice for exams...

s=[] #global declaration of list s

@csrf_exempt
def first(request):
	return render_to_response('first.html')

@csrf_exempt
def next1(request):
    s.append(int(request.POST['s']))
    print(s[0])
    return render_to_response('second.html')

@csrf_exempt
def inputs(request):
	x=int(request.POST["x"])
	y=int(request.POST["y"])
	g=gps()
	g.x=x
	g.y=y
	g.save()
	return render_to_response('second.html')

@csrf_exempt
def graph1(request):
    list_x=gps.objects.values_list('x',flat=True)
    list_y=gps.objects.values_list('y',flat=True)
    plt.plot(list_x,list_y)
    plt.show()
    return render_to_response('second.html')
    
@csrf_exempt
def graph2(request):
    list_x=gps.objects.values_list('x',flat=True)
    list_y=gps.objects.values_list('y',flat=True)
    nos=len(list_x)
    dist=[]
    eqn=0
    for i in range(0,nos-1):
        eqn=math.sqrt(((list_x[i+1]-list_x[i])**2)+((list_y[i+1]-list_y[i])**2))
        dist.append(eqn)
    distance=sum(dist)
    v=distance/(s[0]*nos)
    for i in range(0,nos-1):
        t=(s[0]*i)
        plt.plot(v,t)
        print(t)
    plt.show()
    return render_to_response('second.html')
