from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie

# Create your views here.

def home(request):
    return render(request, 'home.html')

def movies_index(request):
    return render(request, 'movies/index.html')

def movies_detail(request):
    return render(request, 'movies/detial.html')

#def movies_add(request):
#   return render(request, 'movies/add')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class AddMovie(CreateView):
   model = Movie
   fields = ['name', 'genre', 'description', 'release_year',]

  