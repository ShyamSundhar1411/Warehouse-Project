from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.getRoutes,name = "get_attendance_routes"),
]