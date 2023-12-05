from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from StuManageApp import models
from StuManageApp.dao import CourseScore_Service # 自定义服务
from StuManageApp.dao import Student_Service
from StuManageApp.dao import Course_Service
# Create your views here.


def test(request):
    stu_obj = models.Student.objects.all().values()
    return render(request, 'test.html', {'stu':stu_obj})

@csrf_exempt
def index(request): # 初始登录页
    return render(request, 'login.html')

@csrf_exempt
def login(request): # 执行登录功能
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usertype = request.POST['usertype'] # 判断管理员还是学生
    if(usertype=='2'): # 学生登录
        stu_obj = models.Student.objects.all().values().filter(stuNo=username, password=password)
        print(stu_obj)
        if stu_obj:
            response = redirect('/stu/')
            response.set_cookie('username', username)
            return response
        else:
            return render(request, 'login.html', {"error_msg":"用户名或密码错误！"})
    else: # 管理员登录
        admin_obj = models.Admin.objects.all().values().filter(adminName=username, password=password)
        print(admin_obj)
        if admin_obj:
            response = redirect('/admin/')
            response.set_cookie('username', username)
            return response
        else:
            return render(request, 'login.html', {"error_msg":"用户名或密码错误！"})

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
def admin_stu_delete(request): # 管理员注销学生账号
    if request.method == 'GET':
        stuNo = request.GET.get('stuNo')
        flag = Student_Service.delete_student_by_stuNo(stuNo)
        if(flag):
            return redirect('/admin_stu_info/')
        else:
            return HttpResponse('注销失败')

@csrf_exempt
def admin_course_info(request): # 管理员查看课程基本信息
    if request.method == 'GET':
        course_obj = Course_Service.query_course_all()
 
    return render(request, 'Admin_course_info.html', {'courses': course_obj})

@csrf_exempt
def admin_course_score(request): # 管理员查看所有开课课程成绩情况
    if request.method == 'GET':
        course_obj = Course_Service.query_course_all()
        print(course_obj)
 
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
        courseGrade = Course_Service.get_course_grade_by_courseNo
        return render(request, 'Admin_course_score_stu_add.html', {'courseNo':courseNo, 'stuNo':stuNo, 'courseGrade':courseGrade})

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
def stu_select_course(request):
    stuNo = request.COOKIES.get('username')
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