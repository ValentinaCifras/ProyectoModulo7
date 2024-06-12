from django.urls import path
from .views import (index,register,profile,register_profile,update_profile,register_inmueble,
                    get_inmuebles,update_inmueble,contact,messages,disponibles,acerca)
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('',index, name='home'),
    path('login/', LoginView.as_view(next_page='profile'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('profile/',profile, name='profile'),
    path('register_profile/',register_profile, name='register_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('register_inmueble/<str:username>/', register_inmueble, name='register_inmueble'),
    path('inmuebles/', get_inmuebles, name='get_inmuebles'),
    path('inmueble/<int:pk>/', update_inmueble, name='update_inmueble'),
    path('contact/<int:id>/', contact, name='contact'),
    path('messages/', messages, name='mensaje'),
    path('disponibles/', disponibles, name='disponibles'),
    path('acerca/', acerca, name='acerca'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico')))
 
]
