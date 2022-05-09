from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSeriaizer
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSeriaizer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSeriaizer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSeriaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSeriaizer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'complete data updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSeriaizer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial data updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.all(pk=id)
        stu.delete()
        return Response({'msg': 'data deleted'})





