from rest_framework import generics
from .models import Framework
from .serializers import FrameworkSerializer
from textblob import TextBlob
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FrameworkListCreate(generics.ListCreateAPIView):
    queryset = Framework.objects.all()
    serializer_class = FrameworkSerializer


class FrameworkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Framework.objects.all()
    serializer_class = FrameworkSerializer


class SentimentAnalysisView(APIView):
    def post(self, request, format=None):
        # Récupère le texte de la requête
        text = request.data.get('text', '')

        # Analyse de sentiment
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity  # -1 (négatif) à 1 (positif)

        # Renvoie le résultat
        result = {
            'text': text,
            'sentiment': 'positif' if sentiment > 0 else 'négatif' if sentiment < 0 else 'neutre',
            'polarity': sentiment
        }
        return Response(result, status=status.HTTP_200_OK)
