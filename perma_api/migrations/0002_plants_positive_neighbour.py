# Generated by Django 4.2.10 on 2024-02-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perma_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plants',
            name='positive_neighbour',
            field=models.ManyToManyField(blank=True, null=True, to='perma_api.plants'),
        ),
    ]