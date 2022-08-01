from django.urls import path
from blog.views import PostDetailView, PostListView, SearchView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('topics/<slug:slug>/', PostListView.as_view(), name='list_by_topic'),
    path('search/', SearchView.as_view(), name="search_list"),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
