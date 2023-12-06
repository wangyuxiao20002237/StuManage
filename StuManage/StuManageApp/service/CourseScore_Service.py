from StuManageApp import models
from django.db import connection

def query_score_by_stuNo(id): #多表查询学生成绩
    with connection.cursor() as cur:
        cur.execute('''select distinct A.courseNo, courseName, stuScore, A.courseGrade 
                        from stumanageapp_course A, stumanageapp_coursescore B 
                        where A.courseNo = B.courseNO and stuNo=%s and stuScore!='';''', id)
        result = cur.fetchall()
        scores = []
        for item in result: # 元组转换为字典结构
            coursescore={}
            coursescore['courseNo']=item[0]
            coursescore['courseName']=item[1]
            coursescore['stuScore']=item[2]
            coursescore['courseGrade']=item[3]
            scores.append(coursescore)

        cur.execute('''select distinct A.courseNo, courseName, stuScore, A.courseGrade 
                        from stumanageapp_course A, stumanageapp_coursescore B 
                        where A.courseNo = B.courseNO and stuNo=%s and stuScore='';''', id)
        result = cur.fetchall()
        no_scores = []
        for item in result: # 元组转换为字典结构
            coursescore={}
            coursescore['courseNo']=item[0]
            coursescore['courseName']=item[1]
            coursescore['stuScore']=item[2]
            coursescore['courseGrade']=item[3]
            no_scores.append(coursescore)

        return [scores, no_scores]
    
def query_selected_course_by_stuNo(id):
    courseNos = models.CourseScore.objects.all().values('courseNo').filter(stuNo=id) # 已经选了的课程
    selected_courses = []
    for item in courseNos:
        courseNo = item['courseNo']
        select_course = models.Course.objects.all().values().filter(courseNo=courseNo)[0] #去掉最外层括号
        selected_courses.append(select_course)
    return selected_courses

def query_course_can_be_selected_by_stuNo(id): #查询学生还可以选择的课程（排除已经选择的课程）
    stuGrade = models.Student.objects.all().values('stuGrade').filter(stuNo=id)[0]['stuGrade'] # 注意stuGrade的赋值方式,获取学生的年级
    selected_courses = models.CourseScore.objects.all().values('courseNo').filter(stuNo=id) # 已经选了的课程
    courses = models.Course.objects.all().values('courseNo').filter(courseGrade=stuGrade) # 全部可选的课程
    select_courses = []
    for item in courses:
        if item not in selected_courses:
            courseNo = item['courseNo']
            select_course = models.Course.objects.all().values().filter(courseNo=courseNo)[0] #去掉最外层括号
            select_courses.append(select_course)
    return select_courses

def query_course_student_have_score_by_courseNo(id): #查询某一门课下已经登入成绩的学生及其成绩（排除还未登入成绩的学生）
    courseName = models.Course.objects.all().values('courseName').filter(courseNo=id)[0]['courseName']
    stu_obj = models.CourseScore.objects.filter(courseNo=id).exclude(stuScore='')
    return [courseName, stu_obj]

def query_course_student_not_have_score_by_courseNo(id): #还未登入成绩的学生
    courseName = models.Course.objects.all().values('courseName').filter(courseNo=id)[0]['courseName']
    stu_obj = models.CourseScore.objects.filter(courseNo=id, stuScore='')
    return [courseName, stu_obj]
    
def update_student_score(request):
    courseNo = request.POST['courseNo']
    stuNo = request.POST['stuNo']
    stuScore = request.POST['stuScore']
    flag = models.CourseScore.objects.filter(courseNo=courseNo, stuNo=stuNo).update(stuScore=stuScore)
    return flag
