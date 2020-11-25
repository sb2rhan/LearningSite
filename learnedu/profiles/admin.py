from django.contrib import admin

from .models import Profile, Post, Course


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'birth_date']
    search_fields = ['user', 'birth_date']
    list_filter = ('user', 'birth_date')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['profile', 'title', 'content', 'publish_date']
    search_fields = ['profile', 'title']
    list_filter = ('profile', 'publish_date')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'instructor', 'enroll_count']
    search_fields = ['name']
    list_filter = ('instructor', 'enroll_count')
