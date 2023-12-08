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

# 学生全部功能视图函数，个人信息、选课中心、成绩查询

@csrf_exempt
def stu(request): #
    stuNo = request.COOKIES.get('username')
    return render(request, 'Stu_main.html', {'stuNo':stuNo})

@csrf_exempt
def stu_info(request): #
    stuNo = request.COOKIES.get('username')
    stu = models.Student.objects.filter(stuNo=stuNo)[0]
    return render(request, 'Stu_info.html', {'stu':stu})

@csrf_exempt
def stu_info_modify(request): #
    stuNo = request.COOKIES.get('username')
    flag = Student_Service.check_student_status_by_stuNo(stuNo)
    if flag == '0':
        return HttpResponse('该学号已被注销，无法修改个人信息！')
    else:
        if request.method == 'POST':
            flag = Student_Service.student_info_modify(request)
            if flag == '1':
                return redirect('/stu_info/')
            else:
                return HttpResponse('修改失败')
        
        else:    
            stuNo = request.COOKIES.get('username')
            stu = models.Student.objects.filter(stuNo=stuNo)[0]
            return render(request, 'Stu_info_modify.html', {'stu':stu})

@csrf_exempt
def stu_select_course(request): #学生选课
    stuNo = request.COOKIES.get('username')
    flag = Student_Service.check_student_status_by_stuNo(stuNo) #判断是否被注销
    if flag == '0':
        return HttpResponse('该学号已被注销，无法选课！')
    else:
        courses = CourseScore_Service.query_course_can_be_selected_by_stuNo(stuNo) #查询未选的但可供选择的课程
        selected_courses = CourseScore_Service.query_selected_course_by_stuNo(stuNo)
        return render(request, 'Stu_select_course.html', {'stuNo':stuNo, 'courses':courses, 'selected_courses':selected_courses})

@csrf_exempt
def stu_select_course_submit(request): #提交选课
    stuNo = request.COOKIES.get('username')
    courseNo = request.GET.get('courseNo')
    courseGrade = Course_Service.get_course_grade_by_courseNo(courseNo)
    flag = models.CourseScore.objects.create(courseNo=courseNo, stuNo=stuNo, courseGrade=courseGrade)
    if flag:
        return redirect('/stu_select_course/')
    else:
        return HttpResponse('选课失败')

@csrf_exempt
def stu_score(request):
    stuNo = request.COOKIES.get('username')
    [scores, no_scores] = CourseScore_Service.query_score_by_stuNo(stuNo) # 学生查询自己的成绩
    return render(request, 'Stu_score.html', {'stuNo':stuNo, 'scores':scores, 'no_scores':no_scores})