from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .serializer import PostSerializer
import json
import operator
from functools import reduce
import pytz
from django.utils.timezone import now
from django.db.models import Q
from scrapper_app.models import LinkedinPost
from datetime import datetime
from scrapper_app.utility.utils import dumping_company_data
import requests
# Create your views here.
class ScrappingLinkedinHundred(APIView):
    def get(self,request):
        company_list_numbers = [{"starting":0,"ending":100},
                                {"starting":100,"ending":200},
                                {"starting":200,"ending":300},
                                {"starting":300,"ending":400},
                                {"starting":400,"ending":500},
                                {"starting":500,"ending":600},
                                {"starting":600,"ending":700},
                                {"starting":700,"ending":800},
                                {"starting":800,"ending":900},
                                {"starting":900,"ending":1000},
                                {"starting":1000,"ending":1100},
                                {"starting":1100,"ending":1200},
                                {"starting":1200,"ending":1300},
                                {"starting":1300,"ending":1400},
                                {"starting":1400,"ending":1500},
                                {"starting":1500,"ending":1600},
                                {"starting":1600,"ending":1700},
                                {"starting":1700,"ending":1800},
                                {"starting":1800,"ending":1900},
                                {"starting":1900,"ending":2000},]
        timezone = pytz.timezone('Asia/Kolkata')
        a = datetime.now(tz=timezone)
        timestamp = int(a.strftime("%Y%m%d%H%M%S"))
        for i in company_list_numbers:
            response = requests.get("http://127.0.0.1:8000/api/scrapper_hundred/",data = {"starting":i["starting"],"ending":i["ending"],"timestamp":timestamp})
            print(response.json())
            serializer = PostSerializer(data = response.json(),many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                if i == company_list_numbers[-1]:
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ScrappingLinkedin(APIView):
    def get(self,request):
        response = requests.get("http://127.0.0.1:8000/api/scrapper/")
        print(response.json())
        serializer = PostSerializer(data = response.json(),many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class DumpList(APIView):
    def get(self,request):
        dumping_company_data()
        return Response({"msg":"Work completed"})
    
class QueryPost(APIView):
    def get(self,request):
        if request.data.get("query",[]) == []:
            linkedin_post = LinkedinPost.objects.filter(date_on_create = now())
        else:
            args = []
            for i in request.data["query"]:
                args.append(Q(post_data__contains = i))
            linkedin_post = LinkedinPost.objects.filter(reduce(operator.or_, args),date_on_create = now())
        serializer = PostSerializer(linkedin_post ,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)