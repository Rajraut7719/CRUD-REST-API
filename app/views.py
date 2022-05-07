from django.shortcuts import render

from rest_framework import generics

from .serializer import StudentSerializer
from .models import Student

# class StudentGeneric(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentGeneric(generics.ListAPIView,generics.CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentGeneric(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field ='id'

class StudentGeneric1(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field ='id'


