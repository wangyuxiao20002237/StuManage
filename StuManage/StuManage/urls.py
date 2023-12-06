"""StuManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from StuManageApp import views
from StuManageApp.view import login
from StuManageApp.view import Student
from StuManageApp.view import Admin_stu
from StuManageApp.view import Admin_course
from StuManageApp.view import Admin_score


urlpatterns = [
    #path('admin/', admin.site.urls),

    path('test/', views.test), # 测试页面

    # 登录模块
    path('', login.index),
    path('index/', login.index),
    path('login/', login.login),

    # 管理员主页、管理员学生基本信息管理模块
    path('admin/', Admin_stu.admin), #管理员主页
    path('admin_stu_info/', Admin_stu.admin_stu_info), #以下是管理员学生基本信息管理模块
    path('admin_stu_info_add/', Admin_stu.admin_stu_info_add),
    path('admin_stu_info_modify/', Admin_stu.admin_stu_info_modify),
    path('admin_stu_delete/', Admin_stu.admin_stu_delete),


    path('admin_course_info/', Admin_course.admin_course_info), #管理员课程基本信息管理模块

    # 管理员成绩管理模块
    path('admin_course_score/', Admin_score.admin_course_score), # 查看所有课程的成绩列表
    path('admin_course_score_stu/', Admin_score.admin_course_score_stu), # 查看该门课下的学生成绩
    path('admin_course_score_stu_add/', Admin_score.admin_course_score_stu_add),

    # 学生全部功能模块
    path('stu/', Student.stu),
    path('stu_info/', Student.stu_info),
    path('stu_info_modify/', Student.stu_info_modify),
    path('stu_select_course/', Student.stu_select_course),
    path('stu_select_course_submit/', Student.stu_select_course_submit),
    path('stu_score/', Student.stu_score)
]
