from django.urls import path
from pages import views
from .views import download_csv

urlpatterns = [
    path("", views.home, name='home'),
    path("course", views.course, name='course'),
    path('download_csv/', download_csv, name='download_csv'),
]