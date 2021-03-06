"""platzigram URL Configuration."""

# Django
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)