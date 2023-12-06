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

# 管理员课程成绩管理功能模块

@csrf_exempt
def admin_course_score(request): # 管理员查看所有开课课程成绩情况
    if request.method == 'GET':
        course_obj = Course_Service.query_course_all()
        # print(course_obj)
    return render(request, 'Admin_course_score.html', {'courses': course_obj})

@csrf_exempt
def admin_course_score_stu(request): # 管理员查看某一门课下所有学生的成绩
    if request.method == 'GET':
        courseNo = request.GET.get('courseNo')
        [courseName, stu_have_score] = CourseScore_Service.query_course_student_have_score_by_courseNo(courseNo)
        [courseName, stu_not_have_score] =  CourseScore_Service.query_course_student_not_have_score_by_courseNo(courseNo)
    return render(request, 'Admin_course_score_stu.html', {'courseNo':courseNo, 'courseName':courseName, 'stus': stu_have_score, 'stus_not_have_score':stu_not_have_score})

@csrf_exempt
def admin_course_score_stu_add(request): # 这里需要修改,管理员只能登入学生已经选择课程的成绩
    if request.method == 'POST': #提交登入成绩
        courseNo = request.POST['courseNo']
        flag = CourseScore_Service.update_student_score(request)
        if flag:
            return redirect('/admin_course_score_stu/?courseNo=' + courseNo);
        else:
            return HttpResponse("提交失败,该学生未选这门课程")
    else: # 进入页面
        courseNo = request.GET.get('courseNo')
        stuNo = request.GET.get('stuNo')
        courseGrade = Course_Service.get_course_grade_by_courseNo(courseNo)
        return render(request, 'Admin_course_score_stu_add.html', {'courseNo':courseNo, 'stuNo':stuNo, 'courseGrade':courseGrade})