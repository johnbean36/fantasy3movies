from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies_index, name='index' ),
    path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
    path('movies/add/', views.AddMovie.as_view(), name='add_movie'),
    path('movies/actor/', views.AddActor.as_view(), name='actors'),
    path('movies/production/', views.AddProd_Mem.as_view(), name='production'),
    path('accounts/signup/', views.signup, name='signup'),
    path('movies/actor/<int:pk>/delete/', views.DeleteActor.as_view(), name='delete_actor'),
    path('movies/<int:movie_id>/actor_in_movie/<int:actor_id>/', views.actor_in_movie, name='actor_in_movie'),
]