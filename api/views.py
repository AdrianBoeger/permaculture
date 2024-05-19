from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import PlantSerializer
from perma_api.models import Plants
from api.services import check_neighbours, find_optimal_garden_beds


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET, POST': '/api/plants'},
        {'GET, POST': '/api/plants/id'},
        {'GET': '/api/plants/id/good_neighbours'},
        {'GET': '/api/plants/id/bad_neighbours'},
        {'GET': '/api/plants/good_neighbours'},
        {'GET': '/api/plants/bad_neighbours'},
        {'POST': '/api/plants/find_bad_neighbours'},
        {'POST': '/api/plants/optimal_garden_beds'},
    ]

    return Response(routes)


@api_view(['GET', 'POST'])
def getPlants(request):
    if request.method == 'GET':
        plants = Plants.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getPlant(request, plants_id):

    try:
        plant = Plants.objects.get(pk=plants_id)
    except Plants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        plant = Plants.objects.get(id=plants_id)
        serializer = PlantSerializer(plant, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlantSerializer(plant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


@api_view(['POST'])
def findBad_neighbours(request):
    data = request.data
    result = check_neighbours(data)
    return Response(result)


@api_view(['POST'])
def findOptimal_garden_beds(request):
    data = request.data
    result = find_optimal_garden_beds(data)
    return Response(result)


@api_view(['GET'])
def all_good_neighbours(request):
    plants = Plants.objects.all()
    good_neighbours_dict = {}
    for plant in plants:
        good_neighbours_dict[plant.name] = plant.positive_neighbours.all().values_list('name', flat=True)
    return Response(good_neighbours_dict)


@api_view(['GET'])
def all_bad_neighbours(request):
    plants = Plants.objects.all()
    bad_neighbours_dict = {}
    for plant in plants:
        bad_neighbours_dict[plant.name] = plant.negative_neighbours.all().values_list('name', flat=True)
    return Response(bad_neighbours_dict)