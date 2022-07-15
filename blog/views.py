from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from .models import Blog

# Create your views here.

def CreateBlog(request):
    context ={}
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('blogs')
 
    context['form']= form
    return render(request, "blog.html", context)

def Blogs(request):
    blogs = Blog.objects.all()
    return(render(request, 'blogs.html', {'blogs':blogs}))

def update(request, id):   
    blog = get_object_or_404(Blog, id = id)
    form = BlogForm(request.POST or None, instance = blog)
    if form.is_valid():
        form.save()
        return redirect("blogs") 
    return render(request, "blog.html", {'form':form})

def destroy(request, id):  
    blog = Blog.objects.get(id=id)  
    blog.delete()  
    return redirect("blogs")