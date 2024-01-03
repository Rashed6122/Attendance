from django.urls import path
from pages import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import image_view

urlpatterns = [
    path("", views.home, name='home'),
    path("course", views.course, name='course'),
    path("studentLst", views.image_view, name='studentLst'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)