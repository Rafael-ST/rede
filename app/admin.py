from django.contrib import admin
from .models import Bairro, LiderDeEquipe, Amigo
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin, ExportMixin

class BairroResource(resources.ModelResource):
    class Meta:
        model = Bairro
        fields = ('nome',)
        import_id_fields = []


class BairroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BairroResource

admin.site.register(Bairro, BairroAdmin)
admin.site.register(LiderDeEquipe)
admin.site.register(Amigo)
