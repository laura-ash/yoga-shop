from django.shortcuts import render
from .models import Post

def blog_home(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'blog/blog_home.html', {'posts': posts})
