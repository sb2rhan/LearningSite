from django.contrib import admin
from .models import News, Theme


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'content', 'author']
    search_fields = ['title', 'themes', 'author']
    list_filter = ('themes', 'author', 'publish_date')


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
