from .models import Student
from .serializers import StudentSeriaizer
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer
