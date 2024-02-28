"""Define URL patterns for the perma_api"""

from django.urls import path, include
from . import views

app_name = 'perma_api'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Page with all plants
    path('plants/', views.plants, name='plants'),
    path('plants/<int:plants_id>/', views.single_plant, name='plant'),

]
