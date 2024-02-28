import os
import django
from typing import List

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "permaculture.settings")
django.setup()

# Now you can import Django models and use Django functionalities safely
from perma_api.models import Plants


plants = ['Tomato', 'Parsley', 'Basil', 'Cucumber']


def check_neighbours(garden_bed):
    # Get {plant1: bad_neighbours, plant2: bad_neighbours, etc.} from DB
    bad_neighbours_dict = {}
    for plant in garden_bed:
        plant_info = Plants.objects.get(name=plant)
        bad_neighbours = list(plant_info.negative_neighbours.all().values_list('name', flat=True))
        if len(bad_neighbours) > 0:
            bad_neighbours_dict[plant] = bad_neighbours
        else:
            bad_neighbours_dict[plant] = ''

    bad_neighbours_in_garden_bed = {}
    for plant in garden_bed:
        if bad_neighbours_dict[plant]:
            bad_neighbours = bad_neighbours_dict[plant]
            for bn in bad_neighbours:
                if bn in garden_bed:
                    bad_neighbours_in_garden_bed[plant] = bn
    # Handle empty bad_neighbours_in_garden_bed
    if bad_neighbours_in_garden_bed:
        return bad_neighbours_in_garden_bed
    else:
        return None


print(check_neighbours(plants))
