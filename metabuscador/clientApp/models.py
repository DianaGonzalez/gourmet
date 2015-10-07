from django.db import models

class Record(models.Model):
    url = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    pclav = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    visitas = models.IntegerField(default=0)
