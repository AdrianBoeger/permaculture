from django.urls import path
from api import views

urlpatterns = [
    path('', views.getRoutes),
    path('plants/', views.getPlants),
    path('plants/<int:plants_id>/', views.getPlant),
    path('plants/<int:plants_id>/good_neighbours', views.getGood_neighbours),
    path('plants/<int:plants_id>/bad_neighbours', views.getBad_neighbours),
]
