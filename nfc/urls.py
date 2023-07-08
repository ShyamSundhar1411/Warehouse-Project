from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.routes,name = "get_attendance_routes"),
]