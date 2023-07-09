from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.getRoutes,name = "get_attendance_routes"),
    path("get/users/all/",views.NFCUserAPIView.as_view(),name = "get_nfc_users"),
    path("get/meetings/all/",views.MeetingAPIView.as_view(),name = "get_meetings"),
    path('mark/attendance/',views.mark_attendance,name = "mark_attedance"),
    path("get/attendances/all/",views.AttendanceAPIView.as_view(),name = "get_attendance")
]