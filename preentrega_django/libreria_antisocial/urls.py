from django.urls import path, include

from .views import *


urlpatterns = [
    path('guitarra/', guitarra_form_view, name='crear-guitarra'),
    path('bajo/', bajo_form_view, name='crear-bajo'),
    path('bateria/', bateria_form_view, name='crear-bateria'),
    path('busqueda/', search_view, name='crear-busqueda' )
]
