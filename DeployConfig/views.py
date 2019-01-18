# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import traceback
from DeployConfig.models import DeployConfig
from application.models import App
from server.models import Server
from DeployConfig.ConfigFactory import ConfigFactory
from DeployConfig.deployUtil import DeployUtil

@csrf_exempt
def modify(request):
	request.encoding='utf-8'
	context = {}
	try:
		appId = request.GET['appId']
		srvId = request.GET['srvId']
		app = App.objects.get(id=appId)
		srv = Server.objects.get(id=srvId)
		cfgFactory = ConfigFactory()
		cfg = cfgFactory.getConfig('windows')
		path = cfg.getPath(srvId,appId)
		#cfg.createDir(srvId,appId)
		dc = DeployConfig.objects.get(serverId=srvId,applicationId=appId)
	except DeployConfig.DoesNotExist:
		print('server exception \n:%s'% traceback.format_exc())
		dc = DeployConfig()

	dc.serverId = srvId
	dc.applicationId = appId
	dc.configPath = path
	context['app'] = app
	context['srv'] = srv
	context['dc'] = dc
	return render(request, 'deployConfigModify.html', context)

@csrf_exempt
def view(request):
	request.encoding='utf-8'
	context = {}
	context['view']='true'
	try:
		id = request.GET['id']
		
		dc = DeployConfig.objects.get(id=id) 
		app = App.objects.get(id=dc.applicationId)
		srv = Server.objects.get(id=dc.serverId)
		context['app'] = app
		context['srv'] = srv
		context['dc'] = dc
	except BaseException:
		context['msg']='data fetch error'
		
	return render(request, 'deployConfigModify.html', context)

@csrf_exempt
def lists(request):
	request.encoding='utf-8'
	context = {}
	dplcfgList = DeployConfig.objects.all()
	appList = App.objects.all()
	srvList = Server.objects.all()
	context['dplcfgList'] = dplcfgList
	context['appList'] = appList
	context['srvList'] = srvList
	
	cfglist = []
	for srv in srvList:
		subList = []
		for app in appList:
			dict = {'exist':0}
			dict['app'] = app
			dict['srv'] = srv
			print("srv %s app %s"%(srv.name,app.name))
			for dc in dplcfgList:
				if dc.serverId==srv.id and dc.applicationId == app.id :
					dict['exist'] = 1
					dict['dc'] = dc
			subList.append(dict)
		
		cfglist.append(subList)
	context['cfglist'] = cfglist
	
	return render(request, 'deployConfigLists.html', context)
	#return HttpResponse("<p>数据查询！</p>")
@csrf_exempt
def delete(request):
	request.encoding='utf-8'
	context = {}
	try:
		id = request.GET['id']
		dc = DeployConfig.objects.get(id=id)
		print('dc.id %s'%dc.id)
		print('dc.serverId %d'%dc.serverId)
		print('dc.applicationId %d'%dc.applicationId)
		cfgFactory = ConfigFactory()
		cfg = cfgFactory.getConfig('windows')
		path = cfg.getPath(dc.serverId,dc.applicationId)
		cfg.delDir(dc.serverId,dc.applicationId)
		dc.delete()
	except BaseException:
		print('server exception \n:%s'% traceback.format_exc())
	return HttpResponseRedirect("/deployConfig/lists")
	#return HttpResponse("<p>操作成功！</p>")

@csrf_exempt
def save(request):
	request.encoding='utf-8'
	context = {}

	try:
		dc = DeployConfig()
		id = request.POST['id']
		if(id!=None):
			dc.id=id
		dc.serverId = request.POST['srvId']
		dc.applicationId = request.POST['appId']
		dc.remark = request.POST['remark']
		dc.status = request.POST['status']
		
		dc.deployPath = request.POST['deployPath']
		dc.deployAS = request.POST['deployAS']
		dc.shell = request.POST['shell']
		dc.url = request.POST['url']
		dc.successResponse = request.POST['successResponse']
		
		
		cfgFactory = ConfigFactory()
		cfg = cfgFactory.getConfig('windows')
		path = cfg.getPath(dc.serverId,dc.applicationId)
		cfg.createDir(dc.serverId,dc.applicationId)
		dc.configPath = path
		
		print('dc.serverId'+dc.serverId)
		print('dc.applicationId'+dc.applicationId)
		print('dc.remark'+dc.remark)
		print('dc.status'+dc.status)
		print('dc.configPath'+dc.configPath)
		dc.save()
	except BaseException :
		print('server exception \n:%s'% traceback.format_exc())
		context['msg']='login_error'


	return HttpResponseRedirect("/deployConfig/lists")
	#return HttpResponse("<p>数据添加成功！</p>")
	
@csrf_exempt
def deploy(request):
	request.encoding='utf-8'
	context = {}
	dcId = request.GET['dcId']
	du = DeployUtil()
	du.deploy(dcId)
	#return HttpResponseRedirect("/deployConfig/lists")
	return HttpResponse("<p>部署成功！</p>")
	


