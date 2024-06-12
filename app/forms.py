from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil,Inmueble,Contact



class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'email' : 'Correo',
            'password1' : 'Contraseña',
            'password2' : 'Repita Contraseña',
        }



class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('tipo_usuario','rut','direccion','telefono')
    
class InmuebleForm(forms.ModelForm):

    class Meta:
        model = Inmueble
        fields = (
            'id_tipo_inmueble','id_comuna','id_region','imagen','nombre_inmueble',
            'm2_construido','numero_banos','numero_hab','direccion','descripcion'
        )

        labels= {
            'id_tipo_inmueble':'Tipo de Inmueble',
            'id_comuna':'Comuna',
            'id_region':'Region', 
            'imagen' :'imagen',
            'nombre_inmueble':'Nombre Inmueble',
            'm2_construido':'Metros cuadrados construidos', 
            'numero_banos':'Numero de Baños', 
            'numero_hab':'Numero de habitaciones',
            'direccion':'Direccion',
            'descripcion':'Descripcion', 
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('correo','nombre','mensaje')

