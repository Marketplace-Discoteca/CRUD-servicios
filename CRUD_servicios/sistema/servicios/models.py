from django.db import models

class Servicio(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo')
    ]

    id = models.AutoField(primary_key=True)  # Campo ID con autoincremento
    nombre_servicio = models.CharField(max_length=100)  # NOT NULL
    categoria = models.CharField(max_length=50)  # NOT NULL
    subcategoria = models.CharField(max_length=100, blank=True, null=True)
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    precio_oferta_actual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=8, choices=ESTADO_CHOICES, default='ACTIVO')

    def __str__(self):
        return self.nombre_servicio


