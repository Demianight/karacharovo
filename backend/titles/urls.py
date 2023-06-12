from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TitleViewset, HumanViewset, PlaceViewset


router = SimpleRouter()
router.register(
    'titles',
    TitleViewset,
)
router.register(
    'humans',
    HumanViewset,
)
router.register(
    'places',
    PlaceViewset,
)

urlpatterns = [
    path('api/', include(router.urls))
]
