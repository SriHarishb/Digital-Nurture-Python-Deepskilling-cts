from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course,Student,Enrollment
from .serializers import CourseSerializer,StudentSerializer,EnrollmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    # ModelViewSet auto-generates list/retrieve/create/update/delete (full CRUD)
    # for /courses/ once registered with a DRF router.
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    # Extra custom route: GET /courses/{pk}/students/
    # Not part of the default CRUD set — added via @action so it lives under
    # the same viewset/URL prefix instead of a separate view.
    @action(detail=True,methods=['get'])
    def students(self,request,pk=None):
        course = self.get_object()  # 404s automatically if pk doesn't exist
        enrolled_student = Student.objects.filter(enrollment__course=course)
        serializer = StudentSerializer(enrolled_student,many=True)
        return Response(serializer.data)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
