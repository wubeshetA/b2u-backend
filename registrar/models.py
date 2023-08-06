from django.db import models
# import admin
from django.contrib import admin
# Create your models here.

# create a Student model
class Student(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    
    GENDER_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female'),
    ]
    
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    
    # academic info
    school = models.CharField(max_length=50)
    school_address = models.CharField(max_length=50)
    grade = models.IntegerField()
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    # transcript = models.FileField(upload_to='transcripts')
    
    # tertiary education goals
    intended_major1 = models.CharField(max_length=50)
    intended_major2 = models.CharField(max_length=50)
    intended_major3 = models.CharField(max_length=50)
    
    # essay prompt response
    # essay1 = models.TextField()
    # essay2 = models.TextField()
    
    # @admin.display(ordering='user__first_name')
    # def first_name(self):
    #     return self.user.first_name

    # @admin.display(ordering='user__last_name')
    # def last_name(self):
    #     return self.user.last_name

    # def __str__(self):
    #     return f"{self.user.first_name} {self.user.last_name}"

    # class Meta:
    #     ordering = ['user__first_name', 'user__last_name']
    
class Mentor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    
    GENDER_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50),
    phone = models.CharField(max_length=50),
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    
    # essay questions
    essay1 = models.TextField()
    essay2 = models.TextField()
    essay3 = models.TextField()
    
    
class Attachment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attachments')
    
    attachment = models.FileField(upload_to='attachments/')
    
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.student.id} - {self.attachment.name}"
    
    class Meta:
        ordering = ['student__first_name', 'student__last_name', 'attachment']

