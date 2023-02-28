from rest_framework import serializers

from .models import Sexo

class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sexo
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)

