from rest_framework import serializers

from .models import Sexo
from .models import Grado
from .models import Asignatura
from .models import Municipio
from .models import NivelEducativo
from .models import Modalidad
from .models import Seccion
from .models import Turno
from .models import CentroEducativo
from .models import TipoIngreso
from .models import Ciudad
from .models import Pais
from .models import Idioma
from .models import Etnia
from .models import Discapacidad
from .models import Religion
from .models import Departamento
from .models import DelegacionDepartamental
from .models import Zona
from .models import Barrio


class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sexo
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)

class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grado
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)

class NivelEducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelEducativo
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)

class ModalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidad
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',) 

class CentroEducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroEducativo
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',) 

class TipoIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIngreso
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',) 

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',) 

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',) 

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',) 

class EtniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etnia
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',) 

class DiscapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discapacidad
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',) 

class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',) 

class DelegacionDepartamentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DelegacionDepartamental
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',) 

class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = ('id', 'nombre', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)                                                                                                                              