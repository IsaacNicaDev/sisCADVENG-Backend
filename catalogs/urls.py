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

router.register('api/catalogs/sexo', SexoViewSet, 'sexo'),
router.register('api/catalogs/grado', GradoViewSet, 'grado')
router.register('api/catalogs/asignatura', AsignaturaViewSet, 'asignatura')
router.register('api/catalogs/municipio', MunicipioViewSet, 'municipio')
router.register('api/catalogs/nivelEducativo', NivelEducativoViewSet, 'nivelEducativo')
router.register('api/catalogs/modalidad', ModalidadViewSet, 'modalidad')
router.register('api/catalogs/seccion', SeccionViewSet, 'seccion')
router.register('api/catalogs/turno', TurnoViewSet, 'turno')
router.register('api/catalogs/centroEducativo', CentroEducativoViewSet, 'centroEducativo')
router.register('api/catalogs/tipoIngreso', TipoIngresoViewSet, 'tipoIngreso')
router.register('api/catalogs/ciudad', CiudadViewSet, 'ciudad')
router.register('api/catalogs/pais', PaisViewSet, 'pais')
router.register('api/catalogs/idioma', IdiomaViewSet, 'idioma')
router.register('api/catalogs/etnia', EtniaViewSet, 'etnia')
router.register('api/catalogs/discapacidad', DiscapacidadViewSet, 'discapacidad')
router.register('api/catalogs/religion', ReligionViewSet, 'religion')
router.register('api/catalogs/departamento', DepartamentoViewSet, 'departamento')
router.register('api/catalogs/delegacionDepartamental', DelegacionDepartamentalViewSet, 'delegacionDepartamental')
router.register('api/catalogs/zona', ZonaViewSet, 'zona')
router.register('api/catalogs/barrio', BarrioViewSet, 'barrio')

urlpatterns = router.urls