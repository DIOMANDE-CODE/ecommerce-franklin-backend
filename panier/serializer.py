from rest_framework import serializers
from .models import Chariot

class ChariotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chariot
        fields='__all__'