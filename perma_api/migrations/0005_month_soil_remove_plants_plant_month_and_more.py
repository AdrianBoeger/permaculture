# Generated by Django 4.2.10 on 2024-02-23 08:13

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('perma_api', '0004_rename_negative_neighbour_plants_negative_neighbours_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_name', models.CharField(max_length=20)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil_name', models.CharField(max_length=100)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='plants',
            name='plant_month',
        ),
        migrations.AddField(
            model_name='plants',
            name='plant_month_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perma_api.month'),
        ),
    ]
