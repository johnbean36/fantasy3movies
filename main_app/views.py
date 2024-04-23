from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, Actor, Prod_Mem
from .forms import AssocActorForm, AssocCrew
from django.views.generic import DeleteView, UpdateView
import requests, os

# Create your views here.

# def actor_dropdown(request):
#    actors = Actor.objects.all()
#    return render(request,'movies/detail.html',{
#       'actors': actors
#     })

def home(request):
    return render(request, 'home.html')

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {
       'movies': movies
    })

def poster_search(request):
   return render(request, 'movies/poster.html')

def movies_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    
    if request.method == 'POST':
      actor_form = AssocActorForm(request.POST)
      if actor_form.is_valid():
        selectedActor = actor_form.cleaned_data["actors"]
        movie.actor.add(selectedActor)
        return redirect ('detail', movie_id=movie_id)
      
      crew_form = AssocCrew(request.POST)
      if crew_form.is_valid():
         selectedCrew = crew_form.cleaned_data["crew"]
         movie.prod_mem.add(selectedCrew)
         return redirect ('detail', movie_id=movie_id)
    else:
      actor_form = AssocActorForm(request.POST)
      crew_form = AssocCrew(request.POST)
      actors_in_movie = movie.actor.all()
      actors_not_in_movie = Actor.objects.exclude(id__in=movie.actor.all().values_list('id'))
      crew_in_movie = movie.prod_mem.all()
      crew_not_in_movie = Prod_Mem.objects.exclude(id__in=movie.prod_mem.all().values_list('id'))
  

      return render(request, 'movies/detail.html', {
        'movie': movie,
        'actors_not_in_movie': actors_not_in_movie, 
        "actor_form": actor_form,
        "crew_form": crew_form
      })


def search_id(request, result_id):
   api_token = os.environ.get('TMDB_API_TOKEN')
   url = f"https://api.themoviedb.org/3/movie/{result_id}"
   headers = {
    "accept": "application/json",
    "Authorization": api_token
    }
   response = requests.get(url, headers=headers)
   data = response.json()
   return render(request, 'movies/results.html', {'data': data})

def search(request):
  api_token = os.environ.get('TMDB_API_TOKEN')
  movie_title = request.POST.get('genre')
  url = f'https://api.themoviedb.org/3/search/movie?&query={movie_title}'
  headers = {
    "accept": "application/json",
    "Authorization": api_token
  }
  response = requests.get(url, headers=headers)
  data = response.json()
  print(data)
  return render(request, 'movies/poster.html', {'data': data})



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

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class AddActor(CreateView):
  model = Actor
  fields = ['name', 'dob', 'nationality']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
  #The Django docs say this is how you add custom data to a generic CBV
  def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context["actor_list"] = Actor.objects.all()
     return context

class AddProd_Mem(CreateView):
  model = Prod_Mem
  fields = ['name', 'role']

  def form_valid(self, form):
     form.instance.user = self.request.user
     return super().form_valid(form)
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["prod_list"] = Prod_Mem.objects.all()
    return context

class DeleteActor(DeleteView):
   model = Actor
   success_url = '/movies/actor'

class DeleteProd(DeleteView):
   model = Prod_Mem
   success_url = '/movies/production'

class DeleteMovie(DeleteView):
   model = Movie
   success_url = '/movies'

class MovieUpdate(UpdateView):
   model = Movie
   fields = ['genre', 'description', 'release_year']