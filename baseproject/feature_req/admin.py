from django.contrib import admin
from feature_req import models

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display=('title', 'added', 'updated')

class ProductionAreaAdmin(admin.ModelAdmin):
    list_display=('title', 'added', 'updated')

class FeatureRequestAdmin(admin.ModelAdmin):
    list_display=('title', 'client', 'priority', 'production_area')
    list_display_links = ('title',)

admin.site.site_title = 'Engineering project admin console'
admin.site.site_header = 'Engineering project admin console'

admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.ProductionArea, ProductionAreaAdmin)
admin.site.register(models.FeatureRequest, FeatureRequestAdmin)

