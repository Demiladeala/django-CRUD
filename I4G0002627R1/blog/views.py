from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    

