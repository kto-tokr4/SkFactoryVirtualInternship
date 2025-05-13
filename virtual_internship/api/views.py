from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from .serializers import *


class PerevalAPIView(APIView):
    def get(self, request, id):
        try:
            pereval = get_object_or_404(PerevalAdded, pk=id)
            return Response({'perevals': PerevalAddedSerializer(pereval).data})
        except Exception:
            return Response({'Error': 'Object not found'})

    def post(self, request):
        response = {'status': None, 'message': None, 'id': None}
        if 'level' in request.data:
            level_data = request.data.pop('level')
            request.data.update(level_data)

        pereval_serializer = PerevalAddedSerializer(data=request.data)
        if pereval_serializer.is_valid(raise_exception=True):
            pereval = pereval_serializer.save()
            for image in request.data['images']:
                image_serializer = ImagesSerializer(data=image)
                image_serializer.is_valid(raise_exception=True)
                image = image_serializer.save()
                image.pereval = pereval
                image.save()

            response['status'] = 200
            response['message'] = 'Successfully request'
            response['id'] = pereval.id
            return Response({'response': response})
        else:
            response['status'] = 400
            response['message'] = pereval_serializer.errors
            response['id'] = None
            return Response({'response': response})


class PerevalUpdateAPIView(UpdateAPIView):
    queryset = PerevalAdded.objects.all()
    serializers = PerevalAddedSerializer
