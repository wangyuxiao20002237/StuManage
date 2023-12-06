from StuManageApp import models

def check_login(request):
    username = request.POST['username']
    password = request.POST['password']
    flag = models.Admin.objects.all().values().filter(adminName=username, password=password).exists()
    return flag