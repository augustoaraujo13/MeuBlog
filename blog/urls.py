from django.urls import path, include
from .views import home, sobre, posts

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('sobre', sobre, name='sobre'),
    path('posts', posts, name='posts'),
]
