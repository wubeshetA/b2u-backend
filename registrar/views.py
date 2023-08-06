from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer

from registrar.models import Student

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.prefetch_related('attachemenets').all()
    serializer_class = StudentSerializer
    