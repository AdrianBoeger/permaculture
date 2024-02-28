# Generated by Django 4.2.10 on 2024-02-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('plant_month', models.CharField(max_length=20)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('is_deleted', models.BooleanField()),
            ],
        ),
    ]
