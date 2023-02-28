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
from .serializers import DepartamentoSerializer
from .serializers import zonaSerializer
from .serializers import BarrioSerializer

class SexoViewSet(viewsets.ModelViewSet):
    queryset = Sexo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SexoSerializer

class GradoViewSet(viewsets.ModelViewSet):
    queryset = Grado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GradoSerializer 


