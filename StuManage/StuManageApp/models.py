from django.db import models

# Create your models here.
class Admin(models.Model):
    adminName=models.CharField(max_length=255, primary_key=True)
    password=models.CharField(max_length=255)

class Student(models.Model): # 学生表
    stuNo=models.CharField(max_length=255, primary_key=True)
    stuName=models.CharField(max_length=255)
    stuAge=models.CharField(max_length=255)
    stuSex=models.CharField(max_length=255)
    stuGrade=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    status=models.CharField(max_length=255)

class Course(models.Model): # 课程表
    courseNo=models.CharField(max_length=255, primary_key=True)
    courseName=models.CharField(max_length=255)
    courseGrade=models.CharField(max_length=255)

class CourseScore(models.Model): # 成绩表
    courseNo=models.CharField(max_length=255)
    stuNo=models.CharField(max_length=255, primary_key=True)
    stuScore=models.CharField(max_length=255)
    courseGrade=models.CharField(max_length=255)   

    # courseNo=models.ForeignKey(to=Course, to_field='courseNo', on_delete=models.CASCADE)
    # stuNo=models.ForeignKey(to=Student, to_field='stuNo', on_delete=models.CASCADE)
