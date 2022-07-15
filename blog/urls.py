from django.urls import path
from . import views
urlpatterns = [
    path('', views.CreateBlog, name = 'blog'),
    path('blogs/', views.Blogs, name= 'blogs'),
    path('update/<int:id>', views.update,name= 'update'),  
    path('delete/<int:id>', views.destroy,name= 'delete'), 
    
    
]