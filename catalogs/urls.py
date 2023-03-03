from rest_framework import routers

from .api import GenderViewSet
from .api import GradeViewSet
from .api import SubjectViewSet
from .api import MunicipalityViewSet
from .api import EducationalLevelViewSet
from .api import ModalityViewSet
from .api import SectionViewSet
from .api import ShiftViewSet
from .api import EducationalInstitutionViewSet
from .api import EnrolmentTypeViewSet
from .api import CityViewSet
from .api import CountryViewSet
from .api import LanguageViewSet
from .api import EthnicityViewSet
from .api import DisabilityViewSet
from .api import ReligionViewSet
from .api import DepartamentViewSet
from .api import DepartamentalDelegationViewSet
from .api import ZoneViewSet
from .api import DistrictViewSet

router = routers.DefaultRouter()

router.register('Genders', GenderViewSet, 'Genders'),
router.register('Grades', GradeViewSet, 'Grades')
router.register('Subjects', SubjectViewSet, 'Subjects')
router.register('Municipalities', MunicipalityViewSet, 'Municipalities')
router.register('EducationalLevels', EducationalLevelViewSet, 'EducationalLevels')
router.register('Modalities', ModalityViewSet, 'Modalities')
router.register('Sections', SectionViewSet, 'Sections')
router.register('Shifts', ShiftViewSet, 'Shifts')
router.register('EducationalInstitutions', EducationalInstitutionViewSet, 'EducationalInstitutions')
router.register('EnrolmentTypes', EnrolmentTypeViewSet, 'EnrolmentTypes')
router.register('Cities', CityViewSet, 'Cities')
router.register('Countries', CountryViewSet, 'Countries')
router.register('Languages', LanguageViewSet, 'Languages')
router.register('Ethnicities', EthnicityViewSet, 'Ethnicities')
router.register('Disabilities', DisabilityViewSet, 'Disabilities')
router.register('religions', ReligionViewSet, 'religions')
router.register('Departaments', DepartamentViewSet, 'Departaments')
router.register('DepartamentalDelegations', DepartamentalDelegationViewSet, 'DepartamentalDelegations')
router.register('Zones', ZoneViewSet, 'Zones')
router.register('Districts', DistrictViewSet, 'Districts')

urlpatterns = router.urls