from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin

from rest_framework.viewsets import GenericViewSet

from app.strings.models import PetSerializer, Pet


class PetViewSet(GenericViewSet,  # generic view functionality
                 CreateModelMixin,  # handles POSTs
                 RetrieveModelMixin,  # handles GETs for 1 Pet
                 UpdateModelMixin,  # handles PUTs and PATCHes
                 ListModelMixin):  # handles GETs for many Pet

    serializer_class = PetSerializer
    queryset = Pet.objects.all()
