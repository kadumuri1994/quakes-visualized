# Generated by Django 3.1.7 on 2021-03-26 14:35

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('type', models.CharField(max_length=30)),
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Geometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastupdate', models.DateTimeField()),
                ('magtype', models.CharField(max_length=30)),
                ('evtype', models.CharField(max_length=30)),
                ('lon', models.FloatField()),
                ('auth', models.CharField(max_length=30)),
                ('lat', models.FloatField()),
                ('depth', models.FloatField()),
                ('unid', models.CharField(max_length=50)),
                ('mag', models.FloatField()),
                ('time', models.DateTimeField()),
                ('source_id', models.CharField(max_length=30)),
                ('source_catalog', models.CharField(max_length=30)),
                ('flynn_region', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='SeismicData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=30)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seismogram.data')),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='geometry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seismogram.geometry'),
        ),
        migrations.AddField(
            model_name='data',
            name='properties',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seismogram.properties'),
        ),
    ]
