from datetime import datetime
from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
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
@api_view(['POST'])
def mark_attendance(request):
    data = request.data
    meeting = Meeting.objects.get(id=data['meeting_id'])
    user = NFCUser.objects.get(id=data['user_id'])
    attendance = Attendance.objects.filter(meeting=meeting, user=user).first()

    if attendance:
        attendance.status = data['status']
        formatted_date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
        attendance.date = formatted_date
        attendance.save()
    else:
        formatted_date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
        attendance = Attendance.objects.create(
            meeting=meeting,
            user=user,
            status=data['status'],
            date=formatted_date
        )

    # Return a status code as response
    return Response(status=status.HTTP_200_OK)
        
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
    
    