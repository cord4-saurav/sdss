from .models import Student
from .serializers import StudentSeriaizer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer



class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer