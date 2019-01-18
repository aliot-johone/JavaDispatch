# -*- coding: utf-8 -*-
import threading, time, random,sys,os,shutil
import datetime
import json,urllib.request
from urllib import parse
import http.client as client
import configparser
from subprocess import call

server=''
port=''
me_host=''
task_query = ''
task_update = ''
download=''
workdir=''

#查询任务
def queryTask():
		while 1:
			try:
				url = 'http://%s:%s%s?host=%s'%(server,port,task_query,parse.quote_plus(me_host))
				print('task_query url %s'%url)
				data = urllib.request.urlopen(url).read()
				task = json.loads(data)
				print (task)
				if task['status']==0 :
					report({'action':'updateStatus','status':2})
					tmpThread = threading.Thread(target=deployThread,args=[task])
					tmpThread.start()
				time.sleep(120)
			except Exception as e:
				print(e)



#下载war包到指定路径
def downloadWar(jsonData):
	war = ''
	url = 'http://%s:%s%s?taskId=%s'%(server,port,download,jsonData['taskId'])
	print(url)
	f = urllib.request.urlopen('http://%s:%s%s?taskId=%s'%(server,port,download,jsonData['taskId']))
	newFile = os.path.join(workdir,genName())
	print(newFile)
	with open(newFile, "wb") as code:
		code.write(f.read())
	print('download war %s'%newFile)
	war = newFile
	return war

def genName():
		tm =  datetime.datetime.now()
		TIMESTAMP="%Y%m%d%H%M%S.war"
		return tm.strftime(TIMESTAMP)

#部署war包
def deploy(jsonData,war):
	print('deploy war %s to\n%s'%(war,jsonData['deployPath']))
	path = jsonData['deployPath']
	path = os.path.join(path,'ROOT.war')
	shutil.copy(war, path)
	return True
	
	

def execShell(sh):
	print('execShell %s'%(sh))
	if len(sh)>0:
		rtn  = call(sh)
		print('rtn %d'%rtn)
		return rtn
	else:
		print('shell is empty no need execute!')
		return -2
	
	

def report(msgJson):
	print('report json %s'%(msgJson))
	try:
		conn = client.HTTPConnection(server,port)
		headers = {"Content-Type":"application/json"}
		param = msgJson
		conn.request("POST" ,task_update, json.dumps(param), headers)
		response = conn.getresponse()
		data = response.read()
		print(data)
		conn.close()
	except Exception as e:
		print(e)
	
	
def deployThread(jsonData):
	print("start deployThread....%s"%jsonData)
	try:
		war = downloadWar(jsonData)
		if len(war)>0:
			report({'action':'report','msg':u'下载成功'})
		else:
			report({'action':'report','msg':u'下载失败'})
			return 
		status = deploy(jsonData,war)
		if status==True:
			report({'action':'report','msg':u'部署成功'})
		else:
			report({'action':'report','msg':u'部署失败'})
		
		status = execShell(jsonData["shell"])
		if status==True:
			report({'action':'report','msg':u'重启成功'})
		else:
			report({'action':'report','msg':u'重启成功'})
		
	except Exception as e:
		print(e)
	print("end deployThread....")

def initConfig():
	global server,port,me_host,task_query,task_update,download,workdir
	cfgpath=sys.path[0]+'\config.ini'
	cf = configparser.ConfigParser()
	cf.read(cfgpath)
	server=cf.get("clientConfig", "server")
	port=cf.get("clientConfig", "port")
	me_host=cf.get("clientConfig", "me_host")
	task_query = cf.get("clientConfig", "task_query")
	task_update = cf.get("clientConfig", "task_update")
	download=cf.get("clientConfig", "download")
	workdir=cf.get("clientConfig", "workdir")
	print('server %s port %s me_host %s task_query %s task_update %s'%(server , port, me_host, task_query, task_update))
	
	
initConfig()
thread1 = threading.Thread(target = queryTask)
thread1.start()
time.sleep(1)  #确保线程thread1已经启动
print('start join')
thread1.join()	#将一直堵塞，直到thread1运行结束。
print('end join')