from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class PerevalAPIView(APIView):
    def get(self, request):
        perevals = PerevalAdded.objects.all()
        return Response({'perevals': PerevalAddedSerializer(perevals, many=True).data})

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