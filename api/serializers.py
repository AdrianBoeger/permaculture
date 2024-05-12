from rest_framework import serializers
from perma_api.models import Plants, Months


class MonthsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Months
        fields = '__all__'


class PlantSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/relations/
    # StringRelatedField for the written month, PrimaryKeyRelatedField for the ID
    plant_month = serializers.StringRelatedField(many=False)
    harvest_month = serializers.PrimaryKeyRelatedField(queryset=Months.objects.all())
    positive_neighbours_names = serializers.SerializerMethodField()
    negative_neighbours_names = serializers.SerializerMethodField()

    # no need to serialize, because we just return a list
    def get_positive_neighbours_names(self, obj):
        return [neighbour.name for neighbour in obj.positive_neighbours.all()]

    def get_negative_neighbours_names(self, obj):
        return [neighbour.name for neighbour in obj.negative_neighbours.all()]

    class Meta:
        model = Plants
        # changed the field:positive_neighbours to positive_neighbours_names, etc. otherwise ['__all__'] would do.
        fields = ['id', 'name', 'plant_month', 'harvest_month', 'date_added', 'is_deleted', 'positive_neighbours_names', 'negative_neighbours_names']
