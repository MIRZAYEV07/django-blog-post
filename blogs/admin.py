from django.contrib import admin
from .models import Category, Post

admin.site.register(Category)
admin.site.register(Post)


admin.AdminSite.site_header = 'Blog'

# Register your models here.
