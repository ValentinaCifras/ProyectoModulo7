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


def obtener_inmuebles_por_comuna(comuna):
    select = f"""
            SELECT app_inmueble.id, app_inmueble.nombre_inmueble, app_inmueble.descripcion, app_comuna.nombre_comuna 
            FROM app_inmueble 
            INNER JOIN app_comuna 
            ON app_inmueble.id_comuna_id = app_comuna.id 
            WHERE app_comuna.nombre_comuna like'{comuna}';
            """
    query = Inmueble.objects.raw(select)
    archivo1=open("inmuebles_por_comuna.txt","a",encoding='utf-8')
    for i in query:
       archivo1.write(f" Propiedad: {i.nombre_inmueble}")
       archivo1.write("\n")
       archivo1.write(f" Descripcion: {i.descripcion}")
       archivo1.write("\n")
       archivo1.write(f" Comuna: {i.nombre_comuna}" )
       archivo1.write("\n")
    archivo1.close()

def obtener_inmuebles_por_region(region):
    select = f"""
            SELECT app_inmueble.id,app_inmueble.nombre_inmueble, app_inmueble.descripcion, app_region.nombre_region 
            FROM app_inmueble 
            INNER JOIN app_region 
            ON app_inmueble.id_region_id = app_region.id 
            WHERE app_region.nombre_region like'{region}';
            """
    query = Inmueble.objects.raw(select)
    archivo1=open("inmuebles_por_region.txt","a",encoding='utf-8')
    for i in query:
       archivo1.write(f" Propiedad: {i.nombre_inmueble}")
       archivo1.write("\n")
       archivo1.write(f" Descripcion: {i.descripcion}")
       archivo1.write("\n")
       archivo1.write(f" Comuna: {i.nombre_region}" )
       archivo1.write("\n")
    archivo1.close()




