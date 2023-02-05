import logging
import queue

from rest_framework import views, serializers
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet

from app.strings.models import KeySerializer, Key
from app.strings.keyboss import KeyBoss, KeyJob
from app.movie.movieboss import MovieBoss

key_boss = KeyBoss()

logger = logging.getLogger(__name__)


class KeyView(views.APIView):
    # default post = create

    def post(self, request: Request):
        job = KeyJob()
        return_queue = queue.Queue()
        key_boss.add_work(job, return_queue)
        try:
            id = return_queue.get(True, 30)
        except queue.Full:
            logger.critical('Key Creation Queue is full!!')
            return Response({'id': -1})

        return Response({'id': id})


class KeyViewSet(GenericViewSet,  # generic view functionality
                 None,  # handles POSTs
                 RetrieveModelMixin,  # handles GETs for 1 Keys
                 None,  # No Key Update, use custom url
                 ListModelMixin):  # handles GETs for many Keys

    serializer_class = KeySerializer
    queryset = Key.objects.all()
