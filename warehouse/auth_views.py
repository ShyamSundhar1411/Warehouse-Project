from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for i,v in serializer.items():
            data[i] = v
        return data
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenPairSerializer
    

@api_view((['GET']))
def homeRoutes(request):
    routes = [
        'attendance/system/',
        'contact/book/'
    ]
    return Response(routes)