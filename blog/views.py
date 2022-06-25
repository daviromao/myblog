from blog.models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.filter(status='published')

        return queryset

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    