# StuManage
学生信息管理系统
大概每天上传一次创建一个新的分支

M：models.py定义了4个类，对应数据库中的表

V：views.py中定义了视图函数，后续考虑将其分为view文件夹下的多个文件，全部放在一起有点乱

C：urls.py定义了路由，即前端请求交给哪个视图函数进行处理，相当于controller

对应于MVC设计模式

另外servive文件夹下自定义了一些函数，提供给视图函数进行调用

自己下载后，需要安装python django相关的包，并在settings.py中修改数据库相关配置“DATABASE”中的内容
