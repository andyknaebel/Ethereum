from django.shortcuts import render
from rest_framework import viewsets
from .models import employee
from .serializers import employeeSerializer

class employeeView(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer
