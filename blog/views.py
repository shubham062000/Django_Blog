from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog

# Create your views here.

def CreateBlog(request):
    context ={}
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
 
    context['form']= form
    return render(request, "blog.html", context)

def Blogs(request):
    blogs = Blog.objects.all()
    return(render(request, 'blogs.html', {'blogs':blogs}))