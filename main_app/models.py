from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator

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
    
    def get_absolute_url(self):
        return reverse('actor')
    
class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=2,
        choices=GENRES,
    )
    description = models.TextField(max_length=500)
    release_year = models.IntegerField(
    validators=[
        RegexValidator(
            regex=r'^19\d{2}|20[0-4]\d$', 
            message="Enter a valid year between 1900 and 2049",
        ),
    ],
    error_messages={
        'invalid': 'Enter a valid year between 1900 and 2049',
    }
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prod_mem = models.ManyToManyField(Prod_Mem)
    actor = models.ManyToManyField(Actor)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'movie_id': self.id})
