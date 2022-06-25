from django.contrib import admin
from blog.models import Post
from datetime import datetime

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'status')
    exclude = ('published', 'status')
    actions = ['make_published', 'make_withdrawn']

    @admin.action(description='Make selected posts as published')
    def make_published(self, request, queryset):
        queryset.update(status='published')
        queryset.exclude(published__isnull=False).update(published=datetime.now())

    @admin.action(description='Make selected posts as withdrawn')
    def make_withdrawn(self, request, queryset):
        queryset.update(status='withdrawn')
    

