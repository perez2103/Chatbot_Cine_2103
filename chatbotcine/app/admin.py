from django.contrib import admin

# Register your models here.
from .models import CienciaFiccion,PeliculasCiencia
admin.site.register(CienciaFiccion)
admin.site.register(PeliculasCiencia)