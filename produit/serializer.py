from rest_framework import serializers

from .models import Fruit, Categorie, Image

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fruit
        fields='__all__'


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categorie
        fields='__all__'

class CategorieFruitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fruit
        fields='__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        field='__all__'