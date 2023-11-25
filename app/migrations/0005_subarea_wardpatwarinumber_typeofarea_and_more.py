# Generated by Django 4.2.2 on 2023-11-17 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_district_tehsil'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WardPatwariNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('subarea', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ward_subarea', to='app.subarea')),
            ],
            options={
                'verbose_name': 'WardPatwariNumber',
                'verbose_name_plural': 'WardNumber/PatwariNumber',
            },
        ),
        migrations.CreateModel(
            name='TypeOfArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('tehsil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='typeofarea_tehsil', to='app.tehsil')),
            ],
        ),
        migrations.AddField(
            model_name='subarea',
            name='typeofarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subarea_typeofarea', to='app.typeofarea'),
        ),
        migrations.CreateModel(
            name='SocietyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='society_ward', to='app.wardpatwarinumber')),
            ],
            options={
                'verbose_name': 'SocietyName',
                'verbose_name_plural': 'Mohalla/Colony/Society/Road',
            },
        ),
    ]
