from django.shortcuts import render
from app.models import *

# Create your views here.

def ex(request):
    lot=one.objects.all()
    d={'prints':lot}
    return render(request,'ex.html',d)

def Pr(request):
    lots=two.objects.all()
    d={"Pyar":lots}
    return render(request,'Pr.html',d)