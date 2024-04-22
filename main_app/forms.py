from django.forms import ModelForm
from .models import Movie, Actor
from django import forms

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['genre']

class AssocActorForm(forms.Form):
    actors = forms.ModelChoiceField(queryset = Actor.objects.all())
    