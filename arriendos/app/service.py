from app.models import Usuario, Inmueble,Region, Comuna,Tipo_usuario,Tipo_inmueble, Perfil
from django.contrib.auth.models import User

def obtener_inmuebles():
    inmuebles = Inmueble.objects.all()#obtenemos una lista de todos los inmueble creados
    for inmueble in inmuebles:
        print(inmueble)
    

def crear_inmueble(id_usuario,id_tipo_inmueble,id_comuna,id_region,nombre_inmueble,m2_construido,numero_banos,numero_hab,direccion):
    #primero obtenemos los datos para crear el inmueble
    user = User.objects.get(id =id_usuario)
    tipo_inmueble = Tipo_inmueble.objects.get(id =id_tipo_inmueble)
    comuna = Comuna.objects.get(id =id_comuna)
    region = Region.objects.get(id =id_region)

    nuevo_inmueble = Inmueble(
        id_usuario = user,
        id_tipo_inmueble = tipo_inmueble,
        id_comuna = comuna,
        id_region = region,
        nombre_inmueble = nombre_inmueble,
        m2_construido = m2_construido,
        numero_banos = numero_banos,
        numero_hab = numero_hab,
        direccion = direccion
    )

    nuevo_inmueble.save()
    return nuevo_inmueble
    

def actualizar_inmueble(id_inmueble,nombre_inmueble,m2_construido,numero_banos,numero_hab,direccion):
    inmueble = Inmueble.objects.get(id=id_inmueble) #obtener el id del inmueble
    #campos que puedo modificar
    inmueble.nombre_inmueble = nombre_inmueble
    inmueble.m2_construido = m2_construido
    inmueble.numero_banos = numero_banos
    inmueble.numero_hab = numero_hab
    inmueble.direccion = direccion

    inmueble.save()
    return inmueble

    

def borrar_inmueble(id_inmueble):
    inmueble = Inmueble.objects.get(id=id_inmueble)
    inmueble.delete()
    return obtener_inmuebles()