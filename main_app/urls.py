from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies', views.movies_index, name='index' ),
    path('movies/detail', views.movies_detail, ),
    path('accounts/signup', views.signup, name='signup'),
]