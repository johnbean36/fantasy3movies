from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


def home(request):
    return render(request, 'home.html')

def movies_index(request):
    return render(request, 'movies/index.html')

def movies_detail(request):
    return render (request, 'movies/detail.html')