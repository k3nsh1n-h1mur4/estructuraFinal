from django.contrib import admin

from .models import EstructuraModel

class RegistrationAdmin(admin.ModelAdmin):
    fields = ['id', 'matricula', 'nombre']

admin.site.register(EstructuraModel, RegistrationAdmin)