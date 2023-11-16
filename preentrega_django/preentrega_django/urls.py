from django.contrib import admin
from django.urls import include, path
from preentrega_django.views import saludar, saludar, saludar_con_html, html_greeting


urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludo/", saludar),
    path("saludo2/", saludar),
    path("saludo-html/", saludar_con_html),
    path("html-greeting/", html_greeting),
    path("", include("libreria_antisocial.urls"))
]
