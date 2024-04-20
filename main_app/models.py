from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
GENRES = (
    ('1', 'Action'),
    ('2', 'Adventure'),
    ('3', 'Animation'),
    ('4', 'Comedy'),
    ('5', 'Crime'),
    ('6', 'Documentary'),
    ('7', "Drama"),
    ('8', 'Fantasy'),
    ('9', 'Horror'),
    ('10', 'Musical'),
    ('11', 'Mystery'),
    ('12', 'Romance'),
    ('13', 'Science Fiction'),
    ('14', 'Thriller'),
    ('15', 'War'),
    ('16', 'Western')
)

ROLES = (
    ('D', 'Director'),
    ('S', 'Screen Writer'),
    ('P', 'Producer')
)

class Prod_Mem(models.Model):
    role = models.CharField(
        max_length=1,
        choices=ROLES
    )
    name = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=25)
    dob = models.DateField()
    nationality = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=2,
        choices=GENRES,
    )
    description = models.TextField(max_length=500)
    release_year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prod_mem = models.ManyToManyField(Prod_Mem)
    actor = models.ManyToManyField(Actor)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'movie_id': self.id})


