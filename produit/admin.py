from django.contrib import admin
from .models import Fruit,Categorie,Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display=('image',)

class FruitAdmin(admin.ModelAdmin):
    list_display=('nom_fruit','prix_fruit','quantite','poids','categorie','prix')

class CategorieAdmin(admin.ModelAdmin):
    list_display=('categorie',)

admin.site.register(Fruit,FruitAdmin)
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Image,ImageAdmin)
