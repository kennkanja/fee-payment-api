from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.views.generic import ListView

from student.models import Home, Pay, Student
from student.serializers import PaySerializer, StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer

class PayViewSet(viewsets.ModelViewSet):
    queryset = Pay.objects.all()
    serializer_class = PaySerializer

class HomePageView(ListView):
    model = Home
    extra_context = {
        'students' : Student.objects.all(),
        'pays' : Pay.objects.all()
    }
    
    template_name = 'index.html'