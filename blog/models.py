from django.db import models
from django.conf import settings
# Create your models here.

class Publication(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=50, unique=True)

  def __str__ (self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=50)
  subtitle = models.CharField(max_length=140,
                              blank=True, null=True)
  slug = models.SlugField(max_length=50, unique=True)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  blog = models.ForeignKey(Publication)
  author = models.ForeignKey(settings.AUTH_USER_MODEL)

  class Meta:
    ordering = ['-created']

  def __str__ (self):
    return self.title

class Categories(models.Model):
    categories = models.TextField()

    def __str__ (self):
      return self.categories

class Search(models.Model):
    search = models.TextField()

    def __str__ (self):
      return self.search
