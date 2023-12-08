from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from StuManageApp import models
from StuManageApp.service import CourseScore_Service # 自定义服务
from StuManageApp.service import Student_Service
from StuManageApp.service import Course_Service
from StuManageApp.service import Admin_Service
# Create your views here.

# 这一部分的功能已经全部转移到views文件夹下的.py文件中，不用管这一部分了，可以当做参考

def test(request):
    stu_obj = models.Student.objects.all().values()
    return render(request, 'test.html', {'stu':stu_obj})

