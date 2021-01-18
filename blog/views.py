from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    # this is in case you would like to limit the number of blogs in the view
    # blogs = Blog.objects.order_by('-date')[:5]
    
    blogs = Blog.objects.all()
    return render(request,'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    # grabbing one object only - first import the get_object_or_404
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/detail.html', {'blog':blog})