from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from burgers.serializers import BurgerSerializer
from .models import Burgers

# Create your views here.

class BurgerList(APIView, AllowAny):

    def get(self, request):
        burgers = Burgers.objects.all()
        serializer = BurgerSerializer(burgers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
