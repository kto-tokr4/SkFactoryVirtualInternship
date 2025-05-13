from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class PerevalAPIView(APIView):
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


class PerevalAPIIdView(APIView):
    def get(self, request, id):
        try:
            pereval = PerevalAdded.objects.get(id=id)
            return Response({'perevals': PerevalAddedSerializer(pereval).data})
        except PerevalAdded.DoesNotExist:
            return Response({'Error': 'Object not found'})

    def patch(self, request, id):
        try:
            pereval = PerevalAdded.objects.get(id=id)
            if pereval.status == 'NEW':
                if 'level' in request.data:
                    level_data = request.data.pop('level')
                    request.data.update(level_data)
                pereval_serializer = PerevalAddedSerializer(instance=pereval, data=request.data)
                if pereval_serializer.is_valid():
                    pereval_serializer.save()
                    response = {'state': 1}
                    return Response({'response': response})
                else:
                    response = {'state': 0, 'message': pereval_serializer.errors}
                    return Response({'response': response})
            else:
                return Response({'Error': 'Object status is not "NEW"'})
        except PerevalAdded.DoesNotExist:
            return Response({'Error': 'Object not found'})


class PerevalAPIEmailView(APIView):

    def get(self, request, user_email):
        try:
            perevals = PerevalAdded.objects.get(user__email=user_email)
            return Response({'perevals': PerevalAddedSerializer(perevals).data})
        except PerevalAdded.DoesNotExist:
            return Response({'Error': 'Objects not found'})



