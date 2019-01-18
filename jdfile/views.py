# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.views.decorators.csrf import csrf_exempt
import datetime
import traceback
import os
import urllib
from jdfile.models import JdFile
from jdfile.config import JdFileConfig
from task.models import Task



	
@csrf_exempt
def modify(request):
	request.encoding='utf-8'
	context = {}
	
	try:
		
		menuId = request.GET['menuId']
		navi = request.GET['navi']
		title = request.GET['title']
		legend = request.GET['legend']
		url = request.GET['url']
		
		module = request.GET['module']
		moduleId = request.GET['moduleId']
		
		print("module %s moduleId %s" %(module,moduleId))
		context['navi'] = navi
		context['title'] = title
		context['legend'] = legend
		context['module'] = module
		context['moduleId'] = moduleId
		context['menuId'] = menuId
		context['url'] = urllib.parse.quote_plus(url)
		
	except BaseException:
		print('server exception \n:%s'% traceback.format_exc())
		context['msg']='data fetch error'
	return render(request, 'jdfileModify.html', context)

@csrf_exempt
def view(request):
	request.encoding='utf-8'
	context = {}


@csrf_exempt
def lists(request):
	request.encoding='utf-8'
	context = {}

@csrf_exempt
def delete(request):
	request.encoding='utf-8'
	context = {}


@csrf_exempt
def save(request):
	request.encoding='utf-8'
	context = {}
	navi = request.POST['navi']
	title = request.POST['title']
	legend = request.POST['legend']
	menuId = request.POST['menuId']
	
	context['navi'] = navi
	context['title'] = title
	context['legend'] = legend
	context['menuId'] = menuId
	
	uploadFile = request.FILES.get('file')
	
	context['url'] = urllib.parse.unquote(request.POST['url'])
	
	jdfc = JdFileConfig()
	fileName = jdfc.getNewName(uploadFile.name)
	path = jdfc.getFilePath(fileName)
	print(path)
	f = open(path,'wb')
	for chunk in uploadFile.chunks(chunk_size=1024):
		f.write(chunk)
	f.close()
	
	jdfile = JdFile()
	jdfile.path = path
	jdfile.origin = uploadFile.name
	jdfile.newName = fileName
	jdfile.uploadTime = datetime.datetime.now()
	jdfile.module = request.POST['module']
	jdfile.moduleId = request.POST['moduleId']
	# 0 未部署 1正在部署 2已部署
	jdfile.status=0
	jdfile.save()
	
	
	context['msg'] = '文件%s上传成功！'%uploadFile.name

	return render(request, 'jdfileSuccess.html', context)
	
@csrf_exempt
def downloadTask(request):
	request.encoding='utf-8'
	context = {}
	filename="ROOT.war"
	id = request.GET['taskId']
	task = Task.objects.get(id=id)
	wrapper = FileWrapper(open(task.warPath,'rb'))
	response=HttpResponse(wrapper,content_type='application/octet-stream')
	response['Content-Length']=os.path.getsize(task.warPath)
	response['Content-Disposition']='attachment; filename=%s' % filename
	return response

	