from StuManageApp import models
from django.db import connection

def if_same_stuNo(request): #判断学号是否已经存在
    stuNo = request.POST['stuNo']
    flag = models.Student.objects.all().values().filter(stuNo=stuNo).exists()
    if flag: #非空说明已经被注册
        return '1'
    else:
        return '0'
    
def add_student(request): #为学生注册账号
    stuNo = request.POST['stuNo']
    stuName = request.POST['stuName']
    stuAge = request.POST['stuAge']
    stuSex = request.POST['stuSex']
    stuGrade = request.POST['stuGrade']
    pwd = request.POST['password']
    # print(stuNo,stuName,stuAge,stuSex,stuGrade,pwd)
    if(len(stuNo)==0 or len(stuName)==0 or len(stuAge)==0 or len(stuSex)==0 or len(stuGrade)==0 or len(pwd)==0): #空项
        return '-1'
    elif if_same_stuNo(request) == '1': #已经被注册
        return '-2'
    else:
        flag = models.Student.objects.create(stuNo=stuNo, stuName=stuName, stuAge=stuAge, stuSex=stuSex, stuGrade=stuGrade, password=pwd, status='1')
        return flag

def query_student_not_logout():
    result = models.Student.objects.all().values().filter(status='1')
    return result

def query_student_logout(): # 查询被注销的学生
    result = models.Student.objects.all().values().filter(status='0')
    return result

def delete_student_by_stuNo(id):
    flag = models.Student.objects.filter(stuNo=id).update(status='0') # 修改状态位为0表示注销状态
    return flag