"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views as bv

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/show/
    path('show/', bv.index),
    # urls.py中参数采用<类型:变量名>表示,类型不是必须的
    path('delete/<int:article_id>/', bv.delete),
    path('ajax/<int:article_id>/', bv.ajax),
    path('get_id/<int:abc>/', bv.get_id),
    path('save/', bv.html),
    # <>方式是get请求,如果是post请求则不支持
    path('update/', bv.update),
    path('insert/', bv.insert),
]
