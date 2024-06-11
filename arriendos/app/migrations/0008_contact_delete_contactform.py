# Generated by Django 4.2 on 2024-06-06 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_contactform_alter_inmueble_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_inmueble', models.CharField()),
                ('correo', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=64)),
                ('mensaje', models.TextField()),
                ('arrendador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
