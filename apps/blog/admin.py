from django.contrib import admin

from .models import Post, Tag, BannedWord


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('author', 'pub_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(BannedWord)
class BannedWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'reason')
    search_fields = ('word',)
    ordering = ('word',)