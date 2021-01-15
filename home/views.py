from django.shortcuts import render
from blog.models import Post

def index(request):
    posts = Post.objects.all().order_by('date')[:3]
    return render(request, 'home/index.html', {'posts': posts})
