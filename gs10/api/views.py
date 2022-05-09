from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSeriaizer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSeriaizer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSeriaizer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSeriaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSeriaizer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSeriaizer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})






