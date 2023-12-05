from StuManageApp import models
from django.db import connection

def query_course_all():
    result = models.Course.objects.all().values().order_by('courseNo')
    return result

def get_course_grade_by_courseNo(id):
    grade = models.Course.objects.all().values('courseGrade').filter(courseNo=id)[0]['courseGrade']
    return grade
