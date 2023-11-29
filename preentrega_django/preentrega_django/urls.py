from django.contrib import admin
from django.urls import include, path
from preentrega_django.views import saludar, saludar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludo/", saludar),
    path("saludo2/", saludar),
    path("", include("libreria_antisocial.urls"))
]
