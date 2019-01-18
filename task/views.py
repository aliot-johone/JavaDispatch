# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from server.models import Server
from task.models import Task
from django.db.models import F
import traceback
import json

# Create your views here.

@csrf_exempt
def query(request):
	request.encoding='utf-8'
	context = {}
	data = {}
	try:
		host = request.GET['host']
		print('host: %s'%host)
		tasks = Task.objects.filter(host=host,status=0).order_by(F('createTime').desc())
		lens=len(tasks)
		print('len %d'%lens)
		if lens==0:
			data = {'deployPath':''}
		else:
			t = tasks[0]
			data = {'deployAS':t.deployAS,'deployPath':t.deployPath,'shell':t.shell,'status':t.status,'taskId':t.id}
		
	except BaseException:
		print('server exception \n:%s'% traceback.format_exc())
	 #ensure_ascii=False用于处理中文
	return HttpResponse(json.dumps(data,ensure_ascii=False))

@csrf_exempt
def clientReport(request):
	request.encoding='utf-8'
	context = {}
	try:
		req=json.loads(request.body)
		print(req)
		data = {"msg": "ok"}
	except BaseException:
		print('server exception \n:%s'% traceback.format_exc())
	 #ensure_ascii=False用于处理中文
	return HttpResponse(json.dumps(data,ensure_ascii=False))