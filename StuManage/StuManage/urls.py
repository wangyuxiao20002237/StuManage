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

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('test/', views.test), # 测试页面

    path('', views.index),
    path('login/', views.login),

    path('admin/', views.admin),
    path('admin_stu_info/', views.admin_stu_info),
    path('admin_stu_info_add/', views.admin_stu_info_add),
    path('admin_stu_delete/', views.admin_stu_delete),
    path('admin_course_info/', views.admin_course_info),
    path('admin_course_score/', views.admin_course_score), # 查看所有课程的成绩列表
    path('admin_course_score_stu/', views.admin_course_score_stu), # 查看该门课下的学生成绩
    path('admin_course_score_stu_add/', views.admin_course_score_stu_add),

    path('stu/', views.stu),
    path('stu_info/', views.stu_info),
    path('stu_select_course/', views.stu_select_course),
    path('stu_select_course_submit/', views.stu_select_course_submit),
    path('stu_score/', views.stu_score)
]
