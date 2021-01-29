from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('programming/', programming, name='programming'),
    path('articles/', articles, name='articles'),
    path('tutorials/', tutorials, name='tutorials'),
    path('contact/', contact, name='contact'),
]
