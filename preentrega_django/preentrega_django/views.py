from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse



def saludar(request):   
    saludo = "¡Bienvenido a Instrumentos Modern Clix!" 
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

def saludar2(request):
    saludo2= f"Hola Bienvenido a El Mejor Sitio Web De Compras De Instrumentos"
    respuesta_http = HttpResponse(saludo2)
    return respuesta_http
    