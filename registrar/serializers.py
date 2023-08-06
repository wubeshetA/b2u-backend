from rest_framework import serializers
from .models import Student, Mentor, Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        student_id = self.context.get('student_id')
        return Attachment.objects.create(student_id=student_id, **validated_data)
    class Meta:
        model = Attachment
        fields = ['id', 'attachment']
class StudentSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        
        
class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'