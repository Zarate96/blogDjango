from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def home(request):
    queryset = request.GET.get("search")
    posts = Post.objects.filter(state=True)
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset)|
            Q(description__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'title':'Home',
        'image':'img/home-bg.jpg',
        'posts':posts
    }

    return render(request, 'index.html', context)

def programming(request):
    posts = Post.objects.filter(
        state=True,
        category = Category.objects.get(name='Programming')
    )
    context = {
        'title':'Home',
        'image':'img/programming.jpg',
        'posts':posts
    }
    return render(request, 'programming.html', context)

def articles(request):
    posts = Post.objects.filter(
        state=True,
        category = Category.objects.get(name__iexact='Articles')
    )
    context = {
        'title':'Home',
        'image':'img/articles.jpg',
        'posts':posts
    }
    return render(request, 'articles.html', context)

def tutorials(request):
    return render(request, 'tutorials.html', {'title':'Tutorials', 'image':'img/tutorials.jpg'})

def contents(request):
    posts = Post.objects.filter(
        state=True,
        category = Category.objects.get(name__iexact='Contents')
    )
    context = {
        'title':'Contents',
        'image':'img/contents.jpg',
        'posts':posts
    }
    return render(request, 'contents.html', context)

def detallePost(request,slug):
    post = get_object_or_404(Post,slug=slug)
    context = {
        'title': post.title,
        'image': post.image,
        'post': post
    }
    return render(request, 'post.html', context)

def contact(request):
    return render(request, 'contact.html', {'title':'Contact', 'image':'img/contact.jpg'})
