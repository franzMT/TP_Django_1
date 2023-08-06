from typing import Any
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30,null=False)
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    
class TablaProductos(models.Model):
    ORIGEN_CHOICES=[
        ('NAC','Nacional'),
        ('IMP','Importado')
    ]
    nombre = models.CharField(max_length=30,null=False)
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, default=1)
    origen = models.CharField(max_length=3,choices=ORIGEN_CHOICES,default='NAC')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'TablaProducto'
        verbose_name_plural = 'TablaProductos'
    
