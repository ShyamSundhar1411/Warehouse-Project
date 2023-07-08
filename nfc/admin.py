from . models import *
from . resources import *
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class NFCUserAdmin(ImportExportModelAdmin):
    resource_class = NFCUserResource
class MeetingAdmin(ImportExportModelAdmin):
    resource_class = MeetingResource
class AttendanceAdmin(ImportExportModelAdmin):
    resource_class = AttendanceResource
admin.site.register(NFCUser,NFCUserAdmin)
admin.site.register(Meeting,MeetingAdmin)
admin.site.register(Attendance,AttendanceAdmin)
