from django.urls import path
from . import views
urlpatterns = [
    path('', views.CreateBlog, name = 'blog'),
    path('blogs/', views.Blogs, name= 'blogs')
]