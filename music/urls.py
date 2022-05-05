from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.songs_list)
    path('<int:pk>', views.song_details')
]