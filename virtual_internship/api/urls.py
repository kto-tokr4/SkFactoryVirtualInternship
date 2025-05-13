from django.urls import path, include
from .views import PerevalAPIView, PerevalAPIIdView, PerevalAPIEmailView

urlpatterns = [
    path('pereval/email/<str:user_email>/', PerevalAPIEmailView.as_view()),
    path('pereval/<int:id>/', PerevalAPIIdView.as_view()),
    path('pereval/', PerevalAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
