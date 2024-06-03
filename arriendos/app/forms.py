from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil



class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')



class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('tipo_usuario','rut','direccion','telefono')
