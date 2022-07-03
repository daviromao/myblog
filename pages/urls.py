from django.urls import path
from .views import AboutPageView, WorkPageView

app_name = 'pages'

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('works/', WorkPageView.as_view(), name='works'),
]
