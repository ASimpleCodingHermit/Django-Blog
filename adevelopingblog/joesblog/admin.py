from django.contrib import admin
from .models import Post
# Register your models here.

# Registers Posts on the Admin site 
admin.site.register(Post)