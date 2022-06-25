from django.urls import path
from blog.views import PostDetailView, PostListView

urlpatterns = [
    path('', PostListView.as_view()),
    path('<slug:slug>/', PostDetailView.as_view()),
]
