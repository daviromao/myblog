from django.shortcuts import get_object_or_404
from blog.models import Post, Tag
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    tag = None

    def get_queryset(self):
        queryset = Post.objects.filter(status='published')

        tag_slug = self.kwargs.get('slug')

        if tag_slug:
            self.tag = get_object_or_404(Tag, name=tag_slug)
            queryset = queryset.filter(tags=self.tag)

        return queryset

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    