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

router.register('genders', GenderViewSet, 'Genders'),
router.register('grades', GradeViewSet, 'Grades')
router.register('subjects', SubjectViewSet, 'Subjects')
router.register('municipalities', MunicipalityViewSet, 'Municipalities')
router.register('educational-levels', EducationalLevelViewSet, 'EducationalLevels')
router.register('modalities', ModalityViewSet, 'Modalities')
router.register('sections', SectionViewSet, 'Sections')
router.register('shifts', ShiftViewSet, 'Shifts')
router.register('educational-institutions', EducationalInstitutionViewSet, 'EducationalInstitutions')
router.register('enrolment-types', EnrolmentTypeViewSet, 'EnrolmentTypes')
router.register('cities', CityViewSet, 'Cities')
router.register('countries', CountryViewSet, 'Countries')
router.register('languages', LanguageViewSet, 'Languages')
router.register('ethnicities', EthnicityViewSet, 'Ethnicities')
router.register('disabilities', DisabilityViewSet, 'Disabilities')
router.register('religions', ReligionViewSet, 'religions')
router.register('departaments', DepartamentViewSet, 'Departaments')
router.register('departamental-delegations', DepartamentalDelegationViewSet, 'DepartamentalDelegations')
router.register('zones', ZoneViewSet, 'Zones')
router.register('districts', DistrictViewSet, 'Districts')

urlpatterns = router.urls