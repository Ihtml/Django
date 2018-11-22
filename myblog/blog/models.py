from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=32, default='Title')
	content = models.TextField(null=True)
	# 创建对象的时候自动获得当前日期
	pub_time = models.DateTimeField(auto_now=True)
	# pub_time = models.DateTimeField(null=True)
	# 定义后台的标题
	def __str__(self):
		return self.title
