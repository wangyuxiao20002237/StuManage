from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from StuManageApp import models
from StuManageApp.service import CourseScore_Service # 自定义服务
from StuManageApp.service import Student_Service
from StuManageApp.service import Course_Service
from StuManageApp.service import Admin_Service

@csrf_exempt
def admin_course_info(request): # 管理员查看课程基本信息
    if request.method == 'GET':
        course_obj = Course_Service.query_course_all()
 
    return render(request, 'Admin_course_info.html', {'courses': course_obj})