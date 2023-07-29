from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Champion_stats,test
from .serializers import Champion_stats_Serializer,test_Serializer
import json,os
from django.shortcuts import redirect

class StatList(APIView):
    def get(self,request):
        stats=Champion_stats.objects.all()
        serializer = Champion_stats_Serializer(stats,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Champion_stats_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StatDetail(APIView):
    def get_object(self,pk):
        try:
            return Champion_stats.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        stat=self.get_object(pk)
        serializer=Champion_stats(stat)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        stat=self.get_object(pk)
        serializer=Champion_stats(stat,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        stat=self.get_object(pk)
        stat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# def stat_save():
#     with open("./champion.json", "r", encoding='UTF-8-sig') as file:
#         data = json.load(file)
#         print(type(data))
#         print(data)
#     return redirect('/stats/')

class TestList(APIView):
    def get(self,request):
        tests=test.objects.all()
        serializer = test_Serializer(tests,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = test_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data="데미지는 10000"
            return Response({'data':data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TestDetail(APIView):
    def get_object(self,pk):
        try:
            return test.objects.get(pk=pk)
        except test.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        test=self.get_object(pk)
        serializer=test_Serializer(test)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        test=self.get_object(pk)
        serializer=test_Serializer(test,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        test=self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)