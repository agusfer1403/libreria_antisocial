from django.urls import path, include

from .views import guitarra_view
from .views import bajo_view
from .views import bateria_view

from . import views 

urlpatterns = [
    path('guitarra/', guitarra_view, name='guitarra'),
    path('bajo/', bajo_view, name = 'bajo' ),
    path('bateria/',bateria_view, name = 'bateria'),
    path( " ", include( "libreria_antisocial.urls"))
]  