from django.views.generic import TemplateView
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)




class HomeView(TemplateView):
    template_name = "index.html"


from rest_framework.viewsets import GenericViewSet


# class PetViewSet(GenericViewSet,  # generic view functionality
#                  CreateModelMixin,  # handles POSTs
#                  RetrieveModelMixin,  # handles GETs for 1 Company
#                  UpdateModelMixin,  # handles PUTs and PATCHes
#                  ListModelMixin):  # handles GETs for many Companies
#
#     serializer_class = PetSerializer
#     queryset = Pet.objects.all()
