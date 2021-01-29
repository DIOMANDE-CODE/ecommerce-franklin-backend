from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Client
from .serializer import ClientSerializer

# Create your views here.

class ClientList(APIView):

    def get(self,request,format=None):
        client=Client.objects.all()
        serializer=ClientSerializer(client,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)