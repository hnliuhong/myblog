from django.db import models

#  此处定义类对应数据表(必须继承models.Model)
class Article(models.Model):
    # 此处定义的属性,对应数据库的字段
    title = models.CharField(max_length=30, default='default title')
    content = models.TextField(null=True)
