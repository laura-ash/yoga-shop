from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def blog_home(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'blog/blog-home.html', {'posts': posts})

def blog_post(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/blog-post.html', {'post': post})
