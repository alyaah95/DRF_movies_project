from django.db import models

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200)
    
    description = models.TextField()

    release_date = models.DateField()

    poster_image = models.ImageField(upload_to='posters/', null=True, blank=True)

    class Meta:
        abstract=True


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Cast(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(Content):
    categories = models.ManyToManyField(Category, related_name='movies')
    casts = models.ManyToManyField(Cast, related_name='movie_roles')

    def __str__(self):
        return f"Movie: {self.title}"


class Series(Content):
    categories = models.ManyToManyField(Category, related_name='Series')
    casts = models.ManyToManyField(Cast, related_name='Series_roles')

    def __str__(self):
        return f"Series: {self.title}"





