from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/get/users/all/',
        '/get/user/<string:serial>/',
        '/get/message/all/',
        '/get/attendances/all/',
        '/mark/attendance/',
    ]
    return Response(routes)

@api_view(['GET'])
def getNFCUsers(request):
    users = NFCUser.objects.all()
    serializer = NFCUserSerializer(users, many = True)
    return Response(serializer.data)