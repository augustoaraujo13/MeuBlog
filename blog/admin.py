from django.contrib import admin
from .models import Postagem

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "link", "autor", "criado", "atualizado")
    #Poupula o campo slug com o titulo automaticamente.
    prepopulated_fields = {"link": ("titulo",)}

