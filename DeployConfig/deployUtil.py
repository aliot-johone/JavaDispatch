# -*- coding: utf-8 -*-

import shutil
import os
import traceback
import datetime
from DeployConfig.models import DeployConfig
from application.models import App
from jdfile.models import JdFile
from jdfile.config import JdFileConfig
from server.models import Server
from task.models import Task
from django.db.models import F

class DeployUtil:
	
	oldwarDir='war'
	configDir='config'
	workDir='work'
	newWar = 'newWar'
	
	def deploy(self,dcId):
		dc = DeployConfig.objects.get(id=dcId)
		print('deploy')
		cfgzip = self.getConfig(dc.id)
		war = self.getWar(dc.applicationId)
		print('cfg %s \n war  %s'%(cfgzip,war))
		shutil.rmtree(dc.configPath)
		
		self.unzipWar(war,dc.configPath)
		self.unzipConfig(cfgzip,dc.configPath)
		newWar = self.createWar(dc.configPath)
		self.createTask(dc,newWar)
	
		

	#获取配置文件压缩包
	def getConfig(self,dcId):
		print('get config zip')
		jdfile = JdFile.objects.filter(module='deployConfig',moduleId=dcId).order_by(F("uploadTime").desc())[0]
		return jdfile.path
		

	#获取war包
	def getWar(self,appId):
		print('get war')
		jdfile = JdFile.objects.filter(module='app',moduleId=appId).order_by(F("uploadTime").desc())[0]
		return jdfile.path

	#解压war包
	def unzipWar(self,war,configPath):
		path = self.makePath(configPath,self.oldwarDir)
		name = os.path.basename(war)
		path = os.path.join(path,name)
		shutil.copyfile(war,path)
		print('unzip war to %s' % path)
		work = self.makePath(configPath,self.workDir)
		shutil.unpack_archive(war,work,'zip')

	def unzipConfig(self,cfgzip,configPath):
		path = self.makePath(configPath,self.configDir)
		name = os.path.basename(cfgzip)
		path = os.path.join(path,name)
		shutil.copyfile(cfgzip,path)
		print('unzip config to %s' % path)
		work = self.makePath(configPath,self.workDir)
		shutil.unpack_archive(cfgzip,work,'zip')

	#创建war包
	def createWar(self,configPath,warName='ROOT.war'):
		work = self.makePath(configPath,self.workDir)
		newWar = self.makePath(configPath,self.newWar)
		newWar = os.path.join(newWar,'ROOT')
		print('createWar from %s \n to %s ' %(work,newWar))
		shutil.make_archive(newWar,'zip',work)
		dir = os.path.dirname(newWar)
		newName = os.path.join(dir,warName)
		os.rename('%s.zip'%newWar,newName)
		return newName
		

	#创建md5
	def warMd5(self,war):
		print('md5')


	#添加部署任务
	def createTask(self,dc,war):
		print('createTask')
		server = Server.objects.get(id=dc.serverId)
		task = Task()
		task.serverId = dc.serverId
		task.host = server.host
		task.applicationId = dc.applicationId
		task.dcId = dc.id
		task.warPath = war
		task.deployAS = dc.deployAS
		task.md5val = ''
		task.deployPath = dc.deployPath
		task.shell = dc.shell
		task.status=0
		task.createTime=datetime.datetime.now()
		task.save()
		
	def makePath(self,basePath,dir):
		path = os.path.join(basePath,dir)
		isExists=os.path.exists(path)
		if not isExists:
			# 如果不存在则创建目录
			print(path+' 创建成功')
			# 创建目录操作函数
			os.makedirs(path)
		return path