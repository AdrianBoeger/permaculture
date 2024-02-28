from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PlantSerializer
from perma_api.models import Plants


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/plants'},
        {'GET': '/api/plants/id'},
        {'GET': '/api/plants/id/good_neighbours'},
        {'GET': '/api/plants/id/bad_neighbours'},
    ]

    return Response(routes)


@api_view(['GET', 'POST'])
def getPlants(request):
    plants = Plants.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPlant(request, plants_id):
    plant = Plants.objects.get(id=plants_id)
    serializer = PlantSerializer(plant, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getGood_neighbours(request, plants_id):
    plant = Plants.objects.get(id=plants_id)
    good_neighbours = plant.positive_neighbours.all().values_list('name', flat=True)
    return Response(good_neighbours)


@api_view(['GET'])
def getBad_neighbours(request, plants_id):
    plant = Plants.objects.get(id=plants_id)
    bad_neighbours = plant.negative_neighbours.all().values_list('name', flat=True)
    return Response(bad_neighbours)
