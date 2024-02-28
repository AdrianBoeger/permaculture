from django.shortcuts import render
from .models import Plants


def index(request):
    """The Homepage for parma_api"""
    return render(request, 'perma_api/index.html')


def plants(request):
    """"This is the collection for all plants"""
    # From QuerySet to list, then dict
    plants_list = [value['name'] for value in list(Plants.objects.values('name'))]
    context = {'Plants': plants_list}
    return render(request, 'perma_api/plants.html', context)


def single_plant(request, plants_id):
    """"This is a plant"""
    vegetable = Plants.objects.get(id=plants_id)
    # plant_month already is the month_name and not the month_name_id
    plant_month = vegetable.plant_month
    good_neighbours = vegetable.positive_neighbours.all().values_list('name', flat=True)
    bad_neighbours = vegetable.negative_neighbours.all().values_list('name', flat=True)
    # 'plant', 'month', etc. are used in the hmtl templates
    context = {'plant': vegetable, 'month': plant_month, 'good_neighbours': good_neighbours, 'bad_neighbours': bad_neighbours}
    return render(request, 'perma_api/plant.html', context)
