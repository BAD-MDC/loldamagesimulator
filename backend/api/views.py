from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Champion_stats
from .serializers import Champion_stats_Serializer
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