from django.urls import path, include
from .views import home

app_name = 'blog'

urlpatterns = [
    path('', home, name='home')
]