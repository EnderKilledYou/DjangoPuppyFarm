import logging
import queue

from rest_framework import views, serializers
from rest_framework.response import Response
from rest_framework.request import Request

movie_boss = MovieBoss()


class MovieQueueSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class MovieView(views.APIView):
    def get(self, request: Request):
        result = [{'id': 0}]
        movie_boss.add_work({
            'imgs': request.data['imgs']
        })
        results = MovieQueueSerializer(result, many=True).data
        return Response(
            {"results": results}
        )
