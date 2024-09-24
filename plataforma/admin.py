from django.contrib import admin
from plataforma.models import CentroCusto, TipoContrato, Area, Colaborador

admin.site.register(CentroCusto)
admin.site.register(TipoContrato)
admin.site.register(Area)

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'centro_custo', 'tipo_contrato', 'area', 'cargo', 'email', 'data_entrada', 'data_desligamento', 'link_rastreio')

    list_filter = ('nome',)