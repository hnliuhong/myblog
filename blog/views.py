from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# django中的Views层，类似JSP的Servlet,主要用来处理请求。
# 而jdango中template模板层，才是jsp中的View
# 定义处理业务逻辑的方法
# http请求,不能直接访问index函数,因此需要在urls.py里面配置
def index(request):
    # HttpResponse可以返回字符串,适合无刷新请求
    # a标签,表单的提交都属于有刷新请求,返回的是html页面
    # return HttpResponse("hello django")
    # 不用在使用sql语句,所有的操作都是针对对象
    article = Article.objects.get(id=1)
    return render(request,"index.html",{'article':article})
