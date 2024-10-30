from django.contrib import admin

from .models import EstructuraModel

class EstructuraAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(EstructuraModel, EstructuraAdmin)