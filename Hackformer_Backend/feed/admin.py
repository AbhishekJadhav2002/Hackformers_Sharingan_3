from django.contrib import admin

from .models import Comment, Student, Post

# Register your models here.
admin.site.register(Student)

admin.site.register(Post)

admin.site.register(Comment)
