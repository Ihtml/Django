from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	# 默认3个关联的选项插槽，切不能移除
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	# 添加‘过滤器’侧边栏，允许以pub_daye字段过滤列表
	list_filter = ['pub_date']
	search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)

