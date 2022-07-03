from django.contrib import admin
from blog.models import Post, Tag
from datetime import datetime

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['name',]
    list_editable = ['name',]
    list_display_links = None

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'status', 'tag_list')
    exclude = ('published', 'status')
    actions = ['make_published', 'make_withdrawn']
    list_filter = ['published']

    @admin.action(description='Make selected posts as published')
    def make_published(self, request, queryset):
        queryset.update(status='published')
        queryset.exclude(published__isnull=False).update(published=datetime.now())

    @admin.action(description='Make selected posts as withdrawn')
    def make_withdrawn(self, request, queryset):
        queryset.update(status='withdrawn')
    
    def tag_list(self, obj):
            return ', '.join([tag.name for tag in obj.tags.all()])

