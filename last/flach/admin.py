from django.contrib import admin

from .models import Livre , Auteur


class LivreAdmin(admin.ModelAdmin):
    list_display=("titre", "auteur","quantite")
    list_filter=['titre']
    search_fields=("titre",)
    fields=['quantite','auteur','titre']
    #list_per_page=1

admin.site.register(Livre, LivreAdmin)
admin.site.register(Auteur)