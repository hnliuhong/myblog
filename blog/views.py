from django.shortcuts import render
from django.http import HttpResponse
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
