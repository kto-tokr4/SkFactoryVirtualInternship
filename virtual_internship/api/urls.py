from django.urls import path, include
from .views import PerevalAPIView, PerevalUpdateAPIView

urlpatterns = [
    path('pereval/', PerevalAPIView.as_view()),
    path('pereval/<int:id>/', PerevalAPIView.as_view()),
    # path('pereval/<int:id>/', PerevalUpdateAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
