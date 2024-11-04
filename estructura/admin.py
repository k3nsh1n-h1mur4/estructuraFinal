from django.contrib import admin

from .models import EstructuraModel

class EstructuraAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'nombre']
    search_fields = ['matricula']


admin.site.register(EstructuraModel, EstructuraAdmin)

    