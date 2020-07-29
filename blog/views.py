from django.shortcuts import render,get_object_or_404
from .models import blogProject

def blog_home(request):
    blogobj = blogProject.objects.order_by('-blogdate')[:5]
    return render(request,'blog_home.html',{'blogk':blogobj})

def details(request,blog_id):
    detail=get_object_or_404(blogProject,pk=blog_id)
    return render(request,'details.html',{'id':detail})
