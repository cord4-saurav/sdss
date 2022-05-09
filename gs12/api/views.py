from django.shortcuts import render

from rest_framework.response import Response
from .models import Student
from .serializers import StudentSeriaizer
from rest_framework import status
from rest_framework.views import APIView

class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSeriaizer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSeriaizer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSeriaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


    def put(self, request, pk, fromat=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSeriaizer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, fromat=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSeriaizer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, fromat=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})







