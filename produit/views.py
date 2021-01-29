from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Fruit,Categorie,Image
from .serializer import FruitSerializer,CategorieSerializer,CategorieFruitSerializer,ImageSerializer
# Create your views here.

class ImageList(APIView):
    def get(self,request,format=None):
        image=Image.objects.all()
        serializer=ImageSerializer(image,many=True)
        return Response(serializer.data)

class FruitList(APIView):

    def get(self, request, format=None):
        fruit=Fruit.objects.all()
        serializer=FruitSerializer(fruit,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FruitDetail(APIView):
    def get_object(self,pk):
        try:
            categorie=Fruit.objects
            return Fruit.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        fruit=self.get_object(pk)
        serializer=FruitSerializer(fruit)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        fruit=self.get_object(pk=pk)
        serializer=FruitSerializer(fruit,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fruit = self.get_object(pk)
        fruit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class CategorieList(APIView):

    def get(self,request, format=None):
        categorie=Categorie.objects.all()
        serializer=CategorieSerializer(categorie,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategorieFruitDetail(APIView):

    def get_object(self,pk):
        try:
            categorie=Categorie.objects.get(pk=pk)
            fruits=categorie.fruits.all()
            return fruits
        except:
            raise Http404

    def get(self,request,pk,format=None):
        produits=self.get_object(pk)
        serializer=CategorieFruitSerializer(produits,many=True)
        return Response(serializer.data)
