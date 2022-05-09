from .models import Student
from .serializers import StudentSeriaizer
from rest_framework import viewsets

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer
