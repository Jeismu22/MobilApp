# Generated by Django 5.1.3 on 2024-11-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpeta',
            name='estado',
            field=models.CharField(choices=[('completado', 'Completado'), ('en_proceso', 'En Proceso'), ('pendiente', 'Pendiente'), ('retrasado', 'Retrasado')], default='pendiente', max_length=20),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='estado',
            field=models.CharField(choices=[('completado', 'Completado'), ('en_proceso', 'En Proceso'), ('pendiente', 'Pendiente'), ('retrasado', 'Retrasado')], default='pendiente', max_length=20),
        ),
        migrations.AddField(
            model_name='tarea',
            name='estado',
            field=models.CharField(choices=[('completado', 'Completado'), ('en_proceso', 'En Proceso'), ('pendiente', 'Pendiente'), ('retrasado', 'Retrasado')], default='pendiente', max_length=20),
        ),
    ]