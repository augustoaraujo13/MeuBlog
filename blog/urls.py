from django.urls import path
from .views import home, sobre, contato, postagem
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('sobre', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
    path('post/<int:id>', postagem, name='postagem')
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
