from django.db import models


class Months(models.Model):
    """Months in a year"""
    objects = models.Manager()
    month_name = models.CharField(max_length=20)

    def __str__(self):
        """Return the name of the month"""
        return self.month_name


class Plants(models.Model):
    """A plant is a unique vegetable plant"""
    objects = models.Manager()
    name = models.CharField(max_length=100)
    # Use a clean name, not plant_month_id, because the _id will get added at some point and then it will throw an error because of _id_id
    plant_month = models.ForeignKey('Months', on_delete=models.CASCADE, null=True, related_name='+')
    harvest_month = models.ForeignKey('Months', on_delete=models.CASCADE, null=True, related_name='+')
    date_added = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField()
    positive_neighbours = models.ManyToManyField('self', blank=True)
    negative_neighbours = models.ManyToManyField('self', blank=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class Soil(models.Model):
    """Types of soil"""
    object = models.Manager()
    soil_name = models.CharField(max_length=100)

    def __str__(self):
        """Return the name of the soil"""
        return self.soil_name
