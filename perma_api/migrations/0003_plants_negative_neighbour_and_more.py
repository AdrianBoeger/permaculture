# Generated by Django 4.2.10 on 2024-02-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perma_api', '0002_plants_positive_neighbour'),
    ]

    operations = [
        migrations.AddField(
            model_name='plants',
            name='negative_neighbour',
            field=models.ManyToManyField(blank=True, to='perma_api.plants'),
        ),
        migrations.AlterField(
            model_name='plants',
            name='positive_neighbour',
            field=models.ManyToManyField(blank=True, to='perma_api.plants'),
        ),
    ]
