from django.urls import path
from .views import home, sobre, posts, contato

urlpatterns = [
    path('', home, name='home'),
    path('sobre', sobre, name='sobre'),
    path('posts', posts, name='posts'),
    path('contato', contato, name='contato'),
]
