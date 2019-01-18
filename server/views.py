# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from server.models import Server
import traceback

# Create your views here.

	
@csrf_exempt
def modify(request):
	request.encoding='utf-8'
	context = {}
	
	try:
		id = request.GET['id']
		server = Server.objects.get(id=id) 
		context['server'] = server
	except BaseException:
		context['msg']='data fetch error'
	return render(request, 'serverModify.html', context)

@csrf_exempt
def view(request):
	request.encoding='utf-8'
	context = {}
	context['view']='true'
	try:
		id = request.GET['id']
		
		server = Server.objects.get(id=id) 
		print(server.name)
		context['server'] = server
		print(server.name)
	except BaseException:
		context['msg']='data fetch error'
		
	return render(request, 'serverModify.html', context)

@csrf_exempt
def lists(request):
	request.encoding='utf-8'
	context = {}
	serverList = Server.objects.all()
	context['serverList'] = serverList
	return render(request, 'serverLists.html', context)
	#return HttpResponse("<p>数据查询！</p>")
@csrf_exempt
def delete(request):
	request.encoding='utf-8'
	context = {}
	try:
		id = request.GET['id']
		Server.objects.filter(id=id).delete()
	except BaseException:
		print('server exception \n:%s'% traceback.format_exc())
	return HttpResponseRedirect("/server/lists")

@csrf_exempt
def save(request):
	request.encoding='utf-8'
	context = {}

	try:
		server = Server()
		id = request.POST['id']
		if(id!=''):
			server.id=id;
		
		server.name = request.POST['name']
		server.host = request.POST['host']
		server.account = request.POST['account']
		server.passwd = request.POST['passwd']
		server.remark = request.POST['remark']
		server.status = request.POST['status']
		server.save()
	except BaseException :
		print('server exception \n:%s'% traceback.format_exc())
		context['msg']='login_error'


	return HttpResponseRedirect("/server/lists")
	#return HttpResponse("<p>数据添加成功！</p>")