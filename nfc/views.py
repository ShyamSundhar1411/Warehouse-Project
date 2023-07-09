from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

@api_view((['GET']))
def homeRoutes(request):
    routes = [
        'attendance/system/',
        'contact/book/'
    ]
    return Response(routes)
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/get/users/all/',
        '/get/user/<string:serial>/',
        '/get/meeting/all/',
        '/get/attendances/all/',
        '/mark/attendance/',
    ]
    return Response(routes)

## Class Based Views
class NFCUserAPIView(generics.ListCreateAPIView):
    model = NFCUser
    serializer_class = NFCUserSerializer
    
    def get_queryset(self):
        return NFCUser.objects.all()
    
class MeetingAPIView(generics.ListCreateAPIView):
    model = Meeting
    serializer_class = MeetingSerializer
    
    def get_queryset(self):
        return Meeting.objects.all()
    
class AttendanceAPIView(generics.ListCreateAPIView):
    model = Attendance
    serializer_class = AttendanceSerializer
    
    def get_queryset(self):
        return Attendance.objects.all()
    
    