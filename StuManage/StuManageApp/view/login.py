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

# 登录功能

@csrf_exempt
def index(request): # 初始登录页
    return render(request, 'login.html')

@csrf_exempt
def login(request): # 执行登录功能
    if request.method == 'POST':
        username = request.POST['username']
        usertype = request.POST['usertype'] # 判断管理员还是学生
    if(usertype=='2'): # 学生登录
        flag = Student_Service.check_login(request)
        if flag:
            response = redirect('/stu/')
            response.set_cookie('username', username)
            return response
        else:
            return render(request, 'login.html', {"error_msg":"用户名或密码错误！"})
    else: # 管理员登录
        flag = Admin_Service.check_login(request)
        if flag:
            response = redirect('/admin/')
            response.set_cookie('username', username)
            return response
        else:
            return render(request, 'login.html', {"error_msg":"用户名或密码错误！"})