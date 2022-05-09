from .models import Student
from .serializers import StudentSeriaizer
from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer

class Studentdelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer

class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer

class StudentRV(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer

class StudentRD(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer

class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriaizer