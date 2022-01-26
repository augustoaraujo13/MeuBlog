from django.urls import path
from .views import home, sobre, contato
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('sobre', sobre, name='sobre'),
    path('contato/<int:id>', contato, name='contato'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
