from django.db import models
from django.utils import timezone

class CentroCusto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome
    
class TipoContrato(models.Model):
    tipo_contrato = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tipo_contrato
    
class Area(models.Model):
    area = models.CharField(max_length=100) 

    def __str__(self) -> str:
        return self.area   

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    centro_custo = models.ForeignKey(CentroCusto, on_delete=models.CASCADE)
    tipo_contrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    data_entrada = models.DateTimeField()
    desligado = models.BooleanField(default=False)
    data_desligamento = models.DateTimeField(null=True, blank=True)
    observacao = models.TextField()
    link_rastreio = models.URLField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Se o 'desligado' for True e 'data_desligamento' ainda estiver vazio, salvar a data atual
        if self.desligado and self.data_desligamento is None:
            self.data_desligamento = timezone.now()
        # Se 'desligado' for False, limpar o campo 'data_desligamento    
        elif not self.desligado:
            self.data_desligamento = None   

        super().save(*args, **kwargs)      

    def __str__(self) -> str:
        return self.nome       

    