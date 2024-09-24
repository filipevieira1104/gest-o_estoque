from django.db import models
from plataforma.models import Colaborador

class Notebook(models.Model):
    tipo_armazenamento_choices = (
        ('HDD', 'HDD'),
        ('SSD', 'SSD'),
        ('NVMe M.2', 'NVMe M.2')
    )
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    memoria_ram = models.CharField(max_length=100)
    armazenamento = models.CharField(max_length=100)
    tipo_armazenamento = models.CharField(max_length=10, choices=tipo_armazenamento_choices, default='NVMe M.2')
    serial_number = models.CharField(max_length=100)
    atribuido_a = models.ForeignKey(Colaborador,null=True, blank=True, on_delete=models.CASCADE)
    entregue_data = models.DateField(null=True, blank=True)