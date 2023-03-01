from rest_framework import routers

from .api import SexoViewSet
from .api import GradoViewSet
from .api import AsignaturaViewSet
from .api import MunicipioViewSet
from .api import NivelEducativoViewSet
from .api import ModalidadViewSet
from .api import SeccionViewSet
from .api import TurnoViewSet
from .api import CentroEducativoViewSet
from .api import TipoIngresoViewSet
from .api import CiudadViewSet
from .api import PaisViewSet
from .api import IdiomaViewSet
from .api import EtniaViewSet
from .api import DiscapacidadViewSet
from .api import ReligionViewSet
from .api import DepartamentoViewSet
from .api import DelegacionDepartamentalViewSet
from .api import ZonaViewSet
from .api import BarrioViewSet

router = routers.DefaultRouter()

router.register('sexo', SexoViewSet, 'sexo'),
router.register('grado', GradoViewSet, 'grado')
router.register('asignatura', AsignaturaViewSet, 'asignatura')
router.register('municipio', MunicipioViewSet, 'municipio')
router.register('nivelEducativo', NivelEducativoViewSet, 'nivelEducativo')
router.register('modalidad', ModalidadViewSet, 'modalidad')
router.register('seccion', SeccionViewSet, 'seccion')
router.register('turno', TurnoViewSet, 'turno')
router.register('centroEducativo', CentroEducativoViewSet, 'centroEducativo')
router.register('tipoIngreso', TipoIngresoViewSet, 'tipoIngreso')
router.register('ciudad', CiudadViewSet, 'ciudad')
router.register('pais', PaisViewSet, 'pais')
router.register('idioma', IdiomaViewSet, 'idioma')
router.register('etnia', EtniaViewSet, 'etnia')
router.register('discapacidad', DiscapacidadViewSet, 'discapacidad')
router.register('religion', ReligionViewSet, 'religion')
router.register('departamento', DepartamentoViewSet, 'departamento')
router.register('delegacionDepartamental', DelegacionDepartamentalViewSet, 'delegacionDepartamental')
router.register('zona', ZonaViewSet, 'zona')
router.register('barrio', BarrioViewSet, 'barrio')

urlpatterns = router.urls