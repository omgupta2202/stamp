# Generated by Django 4.2.2 on 2023-11-18 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_subarea_wardpatwarinumber_typeofarea_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='district',
        ),
        migrations.RemoveField(
            model_name='details',
            name='mohalla_colony_name_society_road',
        ),
        migrations.RemoveField(
            model_name='details',
            name='sub_area_type',
        ),
        migrations.RemoveField(
            model_name='details',
            name='tehsil',
        ),
        migrations.RemoveField(
            model_name='details',
            name='type_of_area',
        ),
        migrations.RemoveField(
            model_name='details',
            name='ward_number_patwari_number',
        ),
    ]