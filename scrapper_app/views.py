from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .serializer import PostSerializer
import json
from scrapper_app.utility.utils import dumping_company_data
import requests
# Create your views here.
class ScrappingLinkedin(APIView):
    def get(self,request):
        
        response = requests.get("http://127.0.0.1:8000/api/scrapper/")
        print(response.json())
        serializer = PostSerializer(data = response.json(),many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DumpList(APIView):
    def get(self,request):
        dumping_company_data()
        return Response({"msg":"Work completed"})