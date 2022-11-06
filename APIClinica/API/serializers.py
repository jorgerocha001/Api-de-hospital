from django.forms import ValidationError

from rest_framework import serializers

from API.models import Medico, Consultas

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'


class CadastrarConsultasSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length= 100)

    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError("Nome deve conter pelo menos 3 letras")
        return value

class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = '__all__'