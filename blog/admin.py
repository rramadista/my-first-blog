from django.contrib import admin
from .models import Post

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'published_date')    

admin.site.register(Post, BlogAdmin)