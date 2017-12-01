
from django.contrib import admin
from blog.models import Publication, Post, Categories, Search
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'created', 'blog')
@admin.register(Categories)
class PostAdmin(admin.ModelAdmin):
  list_display = ('categories',)
@admin.register(Search)
class PostAdmin(admin.ModelAdmin):
  list_display = ('search',)
