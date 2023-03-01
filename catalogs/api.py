from rest_framework import viewsets, permissions

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
from .serializers import SexoSerializer
from .serializers import GradoSerializer
from .serializers import AsignaturaSerializer
from .serializers import MunicipioSerializer
from .serializers import NivelEducativoSerializer
from .serializers import ModalidadSerializer
from .serializers import SeccionSerializer
from .serializers import TurnoSerializer
from .serializers import CentroEducativoSerializer
from .serializers import TipoIngresoSerializer
from .serializers import CiudadSerializer
from .serializers import PaisSerializer
from .serializers import IdiomaSerializer
from .serializers import EtniaSerializer
from .serializers import DiscapacidadSerializer
from .serializers import ReligionSerializer
from .serializers import DepartamentoSerializer
from .serializers import DelegacionDepartamentalSerializer
from .serializers import ZonaSerializer
from .serializers import BarrioSerializer

class SexoViewSet(viewsets.ModelViewSet):
    queryset = Sexo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SexoSerializer

class GradoViewSet(viewsets.ModelViewSet):
    queryset = Grado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GradoSerializer 

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsignaturaSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MunicipioSerializer

class NivelEducativoViewSet(viewsets.ModelViewSet):
    queryset = NivelEducativo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NivelEducativoSerializer 

class ModalidadViewSet(viewsets.ModelViewSet):
    queryset = Modalidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ModalidadSerializer 

class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SeccionSerializer 

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TurnoSerializer

class CentroEducativoViewSet(viewsets.ModelViewSet):
    queryset = CentroEducativo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CentroEducativoSerializer

class TipoIngresoViewSet(viewsets.ModelViewSet):
    queryset = TipoIngreso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoIngresoSerializer 

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CiudadSerializer 

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaisSerializer 

class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IdiomaSerializer 

class EtniaViewSet(viewsets.ModelViewSet):
    queryset = Etnia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EtniaSerializer 

class DiscapacidadViewSet(viewsets.ModelViewSet):
    queryset = Discapacidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DiscapacidadSerializer 

class ReligionViewSet(viewsets.ModelViewSet):
    queryset = Religion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReligionSerializer 

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartamentoSerializer 

class DelegacionDepartamentalViewSet(viewsets.ModelViewSet):
    queryset = DelegacionDepartamental.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DelegacionDepartamentalSerializer 

class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ZonaSerializer

class BarrioViewSet(viewsets.ModelViewSet):
    queryset = Barrio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BarrioSerializer
