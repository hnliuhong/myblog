from django.contrib import admin
from .models import Article


# 继承ModelAdmin,并且在注册时与Article捆绑,就可以显示对象的属性信息
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']


# Register your models here.
admin.site.register(Article, ArticleAdmin)
