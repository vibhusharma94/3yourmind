from django.contrib import admin
from apps.company.models import Manufacturer, Company, Material


admin.site.register(Company)
admin.site.register(Material)
admin.site.register(Manufacturer)
