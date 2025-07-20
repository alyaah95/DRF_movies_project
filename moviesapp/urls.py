from django.urls import path
from . import views


urlpatterns = [

    path('movies/', views.movie_list_create, name='movie-list-create'),
    path('movies/<int:pk>/', views.movie_detail_update_delete, name='movie-detail-update-delete'),

    path('series/', views.series_list_create, name='series-list-create'),
    path('series/<int:pk>/', views.series_detail_update_delete, name='series-detail-update-delete'),
]