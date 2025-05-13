from django.urls import path, include
from .views import PerevalAPIView


urlpatterns = [
    path('pereval/', PerevalAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
