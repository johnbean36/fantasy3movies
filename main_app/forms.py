from django.forms import ModelForm
from .models import Movie, Actor, Prod_Mem
from django import forms

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['genre']

class AssocActorForm(forms.Form):
    actors = forms.ModelChoiceField(queryset = Actor.objects.all())
    
class AssocCrew(forms.Form):
    crew = forms.ModelChoiceField(queryset=Prod_Mem.objects.all())