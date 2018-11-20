from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=32, default='Title')
	content = models.TextField(null=True)
	# 定义后台的标题
	def __str__(self):
		return self.title
