from django.db import models
from django.contrib.postgres.fields import ArrayField


class Geometry(models.Model):
    type = models.CharField(max_length=30)
    coordinates = ArrayField(models.FloatField())

    class Meta:
        verbose_name = 'Geometry'
        verbose_name_plural = 'Geometry'


class Property(models.Model):
    lastupdate = models.DateTimeField()
    magtype = models.CharField(max_length=30)
    evtype = models.CharField(max_length=30)
    lon = models.FloatField()
    auth = models.CharField(max_length=30)
    lat = models.FloatField()
    depth = models.FloatField()
    unid = models.CharField(max_length=50)
    mag = models.FloatField()
    time = models.DateTimeField()
    source_id = models.CharField(max_length=30)
    source_catalog = models.CharField(max_length=30)
    flynn_region = models.CharField(max_length=70)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class Data(models.Model):
    type = models.CharField(max_length=30)
    id = models.CharField(max_length=40, primary_key=True)
    geometry = models.ForeignKey(Geometry, on_delete=models.CASCADE)
    properties = models.ForeignKey(Property, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Data'


class SeismicData(models.Model):
    action = models.CharField(max_length=30)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(SeismicData, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'SeismicData'
        verbose_name_plural = 'SeismicData'
