from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Post)
admin.site.register(Comment)
