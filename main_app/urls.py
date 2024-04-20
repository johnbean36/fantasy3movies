from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies_index, name='index' ),
    path('movies/detail/', views.movies_detail, name='details'),
    path('movies/add/', views.AddMovie.as_view(), name='add_movie'),
    path('accounts/signup/', views.signup, name='signup'),
    path('movies/')

]