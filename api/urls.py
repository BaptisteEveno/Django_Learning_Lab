# api/urls.py
from django.urls import path
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import FrameworkListCreate, FrameworkRetrieveUpdateDestroy, SentimentAnalysisView

urlpatterns = [
    path('frameworks/', FrameworkListCreate.as_view(), name='framework-list-create'),
    path('frameworks/<int:pk>/', FrameworkRetrieveUpdateDestroy.as_view(), name='framework-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('sentiment-analysis/', SentimentAnalysisView.as_view(), name='sentiment-analysis'),
]

