from django.contrib import admin

# Register your models here.
from .models import Blog, BlogAuthor

admin.site.register(Blog)
admin.site.register(BlogAuthor)