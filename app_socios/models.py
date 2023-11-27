from django.db import models


class Socio(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    ESTADO_CHOICES = [
        ('V', 'Vigente'),
        ('S', 'Suspendido'),
        ('R', 'Retirado'),
    ]

    nombre = models.CharField(max_length=80)
    fecha_incorporacion = models.DateField()
    ano_nacimiento = models.DateField()
    telefono = models.IntegerField()
    correo_electronico = models.EmailField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)
    observacion = models.TextField(blank=True)

    class Meta:
        db_table = 'Socio'

    def __str__(self):
        return self.nombre
