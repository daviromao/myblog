from django.http import Http404
from django.shortcuts import get_object_or_404
from blog.models import Post, Tag
from django.db.models import Q
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

class SearchView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "blog/post_search.html"

    def get_queryset(self):
        query = self.request.GET.get("q") or ""

        posts_list = Post.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
        )

        return posts_list

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        
        if post.status != 'published' and not self.request.user.is_staff:
            raise Http404

        return post
    