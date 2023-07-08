from .models import *
from import_export import resources,fields,widgets
class NFCUserResource(resources.Resource):
    class Meta:
        model = NFCUser

class MeetingResource(resources.Resource):
    class Meta:
        model = Meeting

class AttendanceResource(resources.Resource):
    class Meta:
        model = Attendance