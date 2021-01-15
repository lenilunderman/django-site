from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blogs(request):
    # this is in case you would like to limit the number of blogs in the view
    # blogs = Blog.objects.order_by('-date')[:5]
    
    blogs = Blog.objects.all()
    return render(request,'blog/all_blogs.html', {'blogs': blogs})