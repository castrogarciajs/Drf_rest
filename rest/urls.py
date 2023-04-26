from rest_framework import routers
from api import ProjectViewSets

router = routers.DefaultRouter()


router.register('api/rest', ProjectViewSets, 'rest')

urlpatterns = router.urls
