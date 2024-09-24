from django.contrib import admin
from .models import Notebook

@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'memoria_ram', 'armazenamento', 'tipo_armazenamento', 'serial_number', 'atribuido_a', 'entregue_data')

    list_filter = ('atribuido_a',)