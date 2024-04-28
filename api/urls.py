from django.urls import path
from api import views

urlpatterns = [
    path('', views.getRoutes),
    path('plants/', views.getPlants),
    path('plants/<int:plants_id>/', views.getPlant),
    path('plants/<int:plants_id>/good_neighbours', views.getGood_neighbours),
    path('plants/<int:plants_id>/bad_neighbours', views.getBad_neighbours),
    path('plants/good_neighbours', views.all_good_neighbours),
    path('plants/bad_neighbours', views.all_bad_neighbours),
    path('plants/find_bad_neighbours', views.findBad_neighbours),
    path('plants/optimal_garden_beds/', views.findOptimal_garden_beds),
]
