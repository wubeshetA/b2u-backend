from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny, IsAuthenticated
from registrar.models import Student, Mentor, Attachment
from .serializers import AttachmentSerializer, StudentSerializer, MentorSerializer

class StudentViewSet(ModelViewSet):
    
    queryset = Student.objects.prefetch_related('attachments').all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    
class MentorViewSet(ModelViewSet):
    
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [AllowAny]
    
    
class AttachmentViewSet(ModelViewSet):
    serializer_class = AttachmentSerializer
    permission_classes = [AllowAny]
    
    def get_serializer_context(self):
        return {'student_id': self.kwargs['student_pk'],}
    def get_queryset(self):
        return Attachment.objects.filter(student_id=self.kwargs['student_pk'])
    