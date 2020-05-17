from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def blog(request):
    blogs = Blog.objects
    print(blogs.all)
    return render(request, 'blog/blog.html', {'blog': blogs})


def detail(request, blog_id):
    dblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {"dblog": dblog})
