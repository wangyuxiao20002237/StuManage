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

# 管理员学生基本信息管理、管理员主页功能模块

@csrf_exempt
def admin(request): # 管理员主页
    return render(request, 'Admin_main.html')

@csrf_exempt
def admin_stu_info(request): # 管理员查看学生信息
    if request.method == 'GET':
        stu_obj = Student_Service.query_student_not_logout()

    return render(request, 'Admin_stu_info.html', {'stus':stu_obj})

@csrf_exempt
def admin_stu_info_add(request): # 管理员为学生注册新账号，即添加学生,不能注册相同学号的学生
    if request.method == 'POST':
        flag = Student_Service.add_student(request)
        if flag == '-1':
            return HttpResponse('不能有空项！')       
        elif flag == '-2':
            return HttpResponse('不能注册相同学号的学生！')
        elif flag:
            return redirect('/admin_stu_info/')
        else:
            return HttpResponse('注册失败！')
    else:
        return render(request, 'Admin_stu_info_add.html')

@csrf_exempt
def admin_stu_info_modify(request): # 管理员修改学生信息
    if request.method == 'POST':
        flag = Student_Service.student_info_modify(request)
        if flag == '1':
            return redirect('/admin_stu_info/')
        else:
            return HttpResponse('修改失败！')
    else:
        stuNo = request.GET.get('stuNo')
        flag = Student_Service.check_student_status_by_stuNo(stuNo)
        if flag == '0':
            return HttpResponse('该学号已被注销，无法修改信息')
        else:
            stu = Student_Service.find_student_by_stuNo(stuNo)
            return render(request, 'Admin_stu_info_modify.html', {'stu':stu})
    

@csrf_exempt
def admin_stu_delete(request): # 管理员注销学生账号
    if request.method == 'GET':
        stuNo = request.GET.get('stuNo')
        flag = Student_Service.delete_student_by_stuNo(stuNo)
        if(flag):
            return redirect('/admin_stu_info/')
        else:
            return HttpResponse('注销失败')