from .models import Student

class StudentSerializer(Student):
    class Meta:
        model = Student
        fields = '__all__'