# -*- coding: utf-8 -*-
# from django.http import HttpResponse
# def hello(resquest):
# 	return HttpResponse('Hello World !')
# def happy(resquest):
# 	return HttpResponse('Happy Python !')

from django.shortcuts import render
 
def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    # 使用render来替代之前使用的HTTPResponse，使用context做参数
	# 键值'hello' 对应了模板中的变量"{{hello}}"
    return render(request, 'hello.html', context)

def happy(request):
	context = {}
	context['happy'] = 'Happy Study Python'
	return render(request, 'hello.html', context)