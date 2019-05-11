from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Article


# django中的Views层，类似JSP的Servlet,主要用来处理请求。
# 而jdango中template模板层，才是jsp中的View
# 定义处理业务逻辑的方法  MVT  MVC
# http请求,不能直接访问index函数,因此需要在urls.py里面配置
def index(request):
    # HttpResponse可以返回字符串,适合无刷新请求
    # a标签,表单的提交都属于有刷新请求,返回的是html页面
    # return HttpResponse("hello django")
    # 不用在使用sql语句,所有的操作都是针对对象
    articles = Article.objects.all()
    # 转发,内部是可以跳转到template.html, 数据通过字典形式存储,
    return render(request, "index.html", {'articles': articles})


# 括号里面的参数一定要和urls中指定的变量相同
# 获取参数两种方法：参数名与urls.py定义的变量名相同,如果参数较多后面也可以直接通过request获取
def delete(request, article_id):
    # orm映射,直接操作对象即可
    print(article_id, type(article_id))
    article = Article.objects.get(pk=article_id)
    # 操作对象,就是操作记录
    article.delete()
    articles = Article.objects.all()
    return render(request, "index.html", {'articles': articles})


# id参数名称必须与urls.py配置名称相同
def get_id(request, abc):
    article = Article.objects.get(pk=abc)
    # 存在数据之间的共享,则采用的是转发模式
    return render(request, "update.html", {'article': article})


def update(request):
    # get post请求都可以通过request数据来获取参数信息
    id = request.POST.get('id')
    # 更新对象就等同于更新记录
    article = Article.objects.get(pk=id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 如果有id则save()会执行更新操作,否则插入操作
    article.save()
    # 转发(render)与重定向区别：重定向是不能够共享request数据
    # from django.http import HttpResponseRedirect
    # 重定向是不应该直接访问index.html，需要通过urls.py中转请求
    return HttpResponseRedirect("/show/")


def insert(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 如果有id会执行插入操作
    article.save()
    # 当前页面,与目标页面不存在数据共享,因此执行重定向
    return HttpResponseRedirect("/show/")


def html(request):
    return render(request, "save.html")
