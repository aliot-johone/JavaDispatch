# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import traceback
from application.models import App


	
@csrf_exempt
def modify(request):
	request.encoding='utf-8'
	context = {}
	
	try:
		id = request.GET['id']
		app = App.objects.get(id=id) 
		context['app'] = app
	except BaseException:
		context['msg']='data fetch error'
	return render(request, 'applicationModify.html', context)

@csrf_exempt
def view(request):
	request.encoding='utf-8'
	context = {}
	context['view']='true'
	try:
		id = request.GET['id']
		
		app = App.objects.get(id=id) 
		context['app'] = app
		print(server.name)
	except BaseException:
		context['msg']='data fetch error'
		
	return render(request, 'applicationModify.html', context)

@csrf_exempt
def lists(request):
	request.encoding='utf-8'
	context = {}
	appList = App.objects.all()
	context['appList'] = appList
	return render(request, 'applicationLists.html', context)
	#return HttpResponse("<p>数据查询！</p>")
@csrf_exempt
def delete(request):
	request.encoding='utf-8'
	context = {}
	try:
		id = request.GET['id']
		App.objects.filter(id=id).delete()
	except BaseException:
		print('server exception \n:%s'% traceback.format_exc())
	return HttpResponseRedirect("/application/lists")

@csrf_exempt
def save(request):
	request.encoding='utf-8'
	context = {}

	try:
		app = App()
		id = request.POST['id']
		if(id!=''):
			app.id=id
		app.name = request.POST['name']
		app.remark = request.POST['remark']
		app.status = request.POST['status']
		
		app.save()
	except BaseException :
		print('server exception \n:%s'% traceback.format_exc())
		context['msg']='login_error'


	return HttpResponseRedirect("/application/lists")
	#return HttpResponse("<p>数据添加成功！</p>")