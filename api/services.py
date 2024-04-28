import os
import django
import collections

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "permaculture.settings")
django.setup()

# Now you can import Django models and use Django functionalities safely
from perma_api.models import Plants


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
        return 'No bad neighbours found'


def find_optimal_garden_beds(plants_list, number_of_beds=1):
    bad_neighbours_dict = {}
    bad_neighbours_list = []
    good_neighbours_dict = {}
    good_neighbours_list = []
    counter_list = []

    for plant in plants_list:
        plant_info = Plants.objects.get(name=plant)

        # create bad neighbours dictionary
        bad_neighbours = list(plant_info.negative_neighbours.all().values_list('name', flat=True))
        # only safe bad neighbours which are also in plants_list
        bad_neighbours = set(bad_neighbours).intersection(set(plants_list))
        if len(bad_neighbours) > 0:
            bad_neighbours_dict[plant] = bad_neighbours
        else:
            bad_neighbours_dict[plant] = ''

        # create good neighbours dictionary
        good_neighbours = list(plant_info.positive_neighbours.all().values_list('name', flat=True))
        # only safe good neighbours which are also in plants_list
        good_neighbours = set(good_neighbours).intersection(set(plants_list))
        if len(good_neighbours) > 0:
            good_neighbours_dict[plant] = good_neighbours
        else:
            good_neighbours_dict[plant] = ''

    plants_list_copy = plants_list.copy()
    for plant in plants_list_copy:
        if plant in good_neighbours_dict.keys():
            sub_good_neighbours_list = []
            sub_good_neighbours_list.append(plant)
            for gn in good_neighbours_dict[plant]:
                sub_good_neighbours_list.append(gn)
            for gn in good_neighbours_dict[plant]:
                if gn in good_neighbours_dict.keys():
                    sub_good_neighbours_list.append(gn)
                    for gnn in good_neighbours_dict[gn]:
                        sub_good_neighbours_list.append(gnn)
                try:
                    plants_list_copy.remove(gn)
                except ValueError:
                    pass
            good_neighbours_list.append(sub_good_neighbours_list)

    print(good_neighbours_list)

    # get max and min from counter
    for gn_list in good_neighbours_list:
        counter = collections.Counter(gn_list)
        counter_list.append(counter)

    print(counter_list)

    new_bed_dict = {}
    while len(new_bed_dict) != len(plants_list):
        for counter in counter_list:
            max_occurrence = max(counter.values())
            for k, v in counter.items():
                if v == max_occurrence:
                    if k not in new_bed_dict.keys():
                        new_bed_dict[k] = counter_list.index(counter)
                        remove_k = k
                    else:
                        pass
            counter.pop(remove_k, None)

    max_beds = max(new_bed_dict.values())
    print(max_beds + 1)
    new_bed = []
    for bed in range(max_beds + 1):
        new_bed.append([])
    for k, v in new_bed_dict.items():
        new_bed[v].append(k)
    # alphabetical order for testing
    for bed in new_bed:
        bed.sort()

    return new_bed


print(find_optimal_garden_beds(['Leeks', 'Tomato', 'Cucumber', 'Lettuce', 'Fennel']))
