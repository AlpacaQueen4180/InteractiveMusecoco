from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path("download_midi/", views.download_midi, name="download_midi"),
]