# Generated by Django 4.2 on 2024-06-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_inmueble_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='imagen',
            field=models.URLField(default='Sin Imagen'),
        ),
    ]