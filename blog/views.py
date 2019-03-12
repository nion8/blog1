from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html', context={'posts': posts})
