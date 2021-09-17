from re import I
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import KeyValueSerializer
from .models import KeyValue
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
# Create your views here.

# class KeyValueApi(APIView):
#     def get(self,request,format = None):
#         val = KeyValue.objects.all()
#         serializer = KeyValueSerializer(val,many=True)
#         return Response(serializer.data) 

class KeyValueApi(viewsets.ModelViewSet):
    queryset = KeyValue.objects.all()
    serializer_class = KeyValueSerializer
    filter_backends = [SearchFilter]
    search_fields = ['key']
