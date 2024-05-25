# Generated by Django 4.2 on 2024-05-25 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmueble',
            old_name='m2_construidos',
            new_name='m2_construido',
        ),
        migrations.RemoveField(
            model_name='comuna',
            name='id_comuna',
        ),
        migrations.RemoveField(
            model_name='region',
            name='id_region',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='rut',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_usuario',
        ),
        migrations.AddField(
            model_name='perfil',
            name='tipo_usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.tipo_usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='id_usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='numero_banos',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='numero_hab',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tipo_inmueble',
            name='tipo',
            field=models.CharField(choices=[('Departamento', 'Departamento'), ('Casa', 'Casa'), ('Parcela', 'Parcela')], default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='tipo_usuario',
            name='tipo',
            field=models.CharField(choices=[('Arrendador', 'Arrendador'), ('Arrendatario', 'Arrendatario')], default=0, max_length=50),
        ),
    ]
