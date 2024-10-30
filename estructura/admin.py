from django.contrib import admin

from .models import EstructuraModel

class EstructuraAdmin(admin.ModelAdmin):
    exclude = ['id, user_id_id']
    
admin.site.register(EstructuraModel, EstructuraAdmin)