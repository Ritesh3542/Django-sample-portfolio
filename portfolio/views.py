from django.shortcuts import render
from .models import Project

def home(request):
    projobjs = Project.objects.all()
    return render(request,'home.html',{'projk':projobjs})
