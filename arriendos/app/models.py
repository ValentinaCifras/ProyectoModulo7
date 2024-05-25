from django.db import models
from django.contrib.auth.models import User 

class Usuario(models.Model):                                       
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.id_usuario.username
    
class Inmueble(models.Model): 
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=0)
    id_tipo_inmueble = models.ForeignKey('Tipo_inmueble', on_delete=models.CASCADE)
    id_comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE)
    nombre_inmueble = models.CharField(max_length=100, null=False, blank=False)
    m2_construido = models.FloatField()
    numero_banos = models.PositiveIntegerField(default=0)
    numero_hab = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre_inmueble}/Direccion:{self.direccion}/ M2:{self.m2_construido}/ Baños: {self.numero_banos} / Habitaciones: {self.numero_hab}"
    
class Region(models.Model):
    CHOICES = [
        ('Arica y Parinacota', 'Arica y Parinacota'),
        ('Tarapaca', 'Tarapaca'),
        ('Antofagasta', 'Antofagasta'),
        ('Atacama', 'Atacama'),
        ('Coquimbo', 'Coquimbo'),
        ('Valparaiso', 'Valparaiso'),
        ('Metropolitana', 'Metropolitana'),
        ('OHiggins', 'OHiggins'),
        ('Maule', 'Maule'),
        ('Nuble', 'Nuble'),
        ('Biobio', 'Biobio'),
        ('La Araucania', 'La Araucania'),
        ('Los Rios', 'Los Rios'),
        ('Los Lagos', 'Los Lagos'),
        ('Aysen', 'Aysen'),
        ('Magallanes', 'Magallanes'),
    ]

    nombre_region = models.CharField(max_length=50,choices=CHOICES, null=False, blank=False)

    def __str__(self):
        return self.nombre_region
    
class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.nombre_comuna
    
class Tipo_inmueble(models.Model):
    CHOICES = [
        ('Departamento', 'Departamento'),
        ('Casa', 'Casa'),
        ('Parcela', 'Parcela'),
    ]
    tipo = models.CharField(max_length=50, choices=CHOICES, default=0)

    def __str__(self):
        return self.tipo
    

class Tipo_usuario(models.Model):
    CHOICES = [
        ('Arrendador', 'Arrendador'),
        ('Arrendatario', 'Arrendatario')
    ]
    tipo = models.CharField(max_length=50,choices=CHOICES, default=0)

    def __str__(self):
        return self.tipo
    
class Perfil(models.Model):
    usuario = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    tipo_usuario = models.ForeignKey('Tipo_usuario', on_delete=models.CASCADE, default=0)
    rut = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    
    def __str__(self):
        return self.usuario.username
