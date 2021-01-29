from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', {'title':'Home', 'image':'img/home-bg.jpg'})

def programming(request):
    return render(request, 'programming.html', {'title':'Programming', 'image':'img/programming.jpg'})

def articles(request):
    return render(request, 'articles.html', {'title':'Articles', 'image':'img/articles.jpg'})

def tutorials(request):
    return render(request, 'tutorials.html', {'title':'Tutorials', 'image':'img/tutorials.jpg'})

def contact(request):
    return render(request, 'contact.html', {'title':'Contact', 'image':'img/contact.jpg'})
