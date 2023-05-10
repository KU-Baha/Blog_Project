from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from .models import Category, Post, Tag, BannedWord


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title'
    )
    list_display_links = (
        'indented_title',
    )
    list_filter = (
        'parent',
    )
    search_fields = (
        'title',
        'description'
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'pub_date'
    )
    list_filter = (
        'author',
        'pub_date'
    )
    search_fields = (
        'title',
        'content'
    )
    date_hierarchy = 'pub_date'
    ordering = (
        '-pub_date',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'name',
    )


@admin.register(BannedWord)
class BannedWordAdmin(admin.ModelAdmin):
    list_display = (
        'word',
        'reason'
    )
    search_fields = (
        'word',
    )
    ordering = (
        'word',
    )
