from django.contrib import admin

# Register your models here.zh_Hansfrom .models import Question,
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content','pub_time')
    # 添加过滤器，按日期过滤
    list_filter = ('pub_time',) # 只有一个成员时要加上逗号 ，

admin.site.register(Article, ArticleAdmin)
