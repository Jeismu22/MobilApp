from django.db import models

class Carpeta(models.Model):
    ESTADO_CHOICES = [
        ('completado', 'Completado'),
        ('en_proceso', 'En Proceso'),
        ('pendiente', 'Pendiente'),
        ('retrasado', 'Retrasado'),
    ]
    titulo = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')  # Agregar el campo de estado
    
    def __str__(self):
        return self.titulo

class Proyecto(models.Model):
    ESTADO_CHOICES = [
        ('completado', 'Completado'),
        ('en_proceso', 'En Proceso'),
        ('pendiente', 'Pendiente'),
        ('retrasado', 'Retrasado'),
    ]
    titulo = models.CharField(max_length=100)
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')  # Agregar el campo de estado
    
    def __str__(self):
        return self.titulo

class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('completado', 'Completado'),
        ('en_proceso', 'En Proceso'),
        ('pendiente', 'Pendiente'),
        ('retrasado', 'Retrasado'),
    ]
    titulo = models.CharField(max_length=100)
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')  # Agregar el campo de estado
    
    def __str__(self):
        return self.titulo
