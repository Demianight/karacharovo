from rest_framework import mixins, viewsets
from .models import Title, Place, Human
from .serializers import TitleSerializer, PlaceSerializer, HumanSerializer


class AbstractViewset(
    viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin
):
    pass


class TitleViewset(AbstractViewset):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class PlaceViewset(AbstractViewset):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class HumanViewset(AbstractViewset):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
