from django.urls import path, include
from .views import *

urlpatterns = [
    path('guitarra/', guitarra_form_view, name='crear-guitarra'),
    path('bajo/', bajo_form_view, name='crear-bajo'),
    path('bateria/', bateria_form_view, name='crear-bateria'),
    path('busqueda/', search_view, name='crear-busqueda'),
    path('guitarra_electrica/', guitarra_electrica_form_view, name='crear-guitarra_electrica'),
    path('listar_guitarras/', listar_guitarras, name='listar_guitarras'),
    path('editar_guitarra/<int:pk>/', editar_guitarra, name='editar_guitarra'),
    path('eliminar_guitarra/<int:pk>/', eliminar_guitarra, name='eliminar_guitarra'),
    path('listar_bajos/', listar_bajos, name='listar_bajos'),
    path('editar_bajo/<int:pk>/', editar_bajo, name='editar_bajo'),
    path('eliminar_bajo/<int:pk>/', eliminar_bajo, name='eliminar_bajo'),
    path("listar_baterias/", listar_baterias, name='listar_baterias'),
    path("editar_bateria/<int:pk>/", editar_bateria, name='editar_bateria'),
    path("eliminar_bateria/<int:pk>/", eliminar_bateria, name='eliminar_bateria'),
    path("listar_guitarras_electricas/", listar_guitarras_electricas, name='listar_guitarras_electricas'),
    path("editar_guitarra_electrica/<int:pk>/", editar_guitarra_electrica, name='editar_guitarra_electrica'),
    path("eliminar_guitarra_electrica/<int:pk>/", eliminar_guitarra_electrica, name='eliminar_guitarra_electrica'),
    path('detalle_guitarra/<int:pk>/', detalle_guitarra, name='detalle_guitarra'),
    path('detalle_bateria/<int:pk>/', detalle_bateria, name='detalle_bateria'),
    path('detalle_guitarra_electrica/<int:pk>/', detalle_guitarra_electrica, name='detalle_guitarra_electrica'),
    path('detalle_bajo/<int:pk>/', detalle_bajo, name='detalle_bajo'),
]
