from django.contrib import admin
from app.models import Usuario, Inmueble, Region, Comuna, Tipo_inmueble, Tipo_usuario, Perfil
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Tipo_inmueble)
admin.site.register(Tipo_usuario)
admin.site.register(Inmueble)
admin.site.register(Perfil)

