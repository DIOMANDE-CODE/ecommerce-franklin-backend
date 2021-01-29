from django.contrib import admin
from .models import Chariot
# Register your models here.

class ChariotAdmin(admin.ModelAdmin):
    list_display=('nom_article_commande','prix_article','quantite','total','date')

admin.site.register(Chariot,ChariotAdmin)