from django.contrib import admin
from .models import *

@admin.register(Urugendo)
class UrugendoAdmin(admin.ModelAdmin):
    list_display = "kuva", "gushika", "date"


admin.site.register(Ingenzi)
admin.site.register(Itike)
