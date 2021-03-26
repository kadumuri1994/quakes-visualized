from django.contrib import admin
from .models import Geometry, Property, Data, SeismicData


class GeometryAdmin(admin.ModelAdmin):
    pass


class PropertyAdmin(admin.ModelAdmin):
    pass


class DataAdmin(admin.ModelAdmin):
    pass


class SeismicDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(Geometry, GeometryAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(SeismicData, SeismicDataAdmin)
