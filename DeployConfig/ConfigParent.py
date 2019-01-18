# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
import shutil

from django.views.decorators.csrf import csrf_exempt
import traceback

class  ConfigParent:
	
	configFolder='configs'
	splitor = '\\'
	
	def createDir(self,srvId,appId):
		path=self.getPath(srvId,appId)
		# 去除尾部 \ 符号
		path=path.rstrip("\\")
		# 判断路径是否存在
		# 存在     True
		# 不存在   False
		isExists=os.path.exists(path)
		# 判断结果
		if not isExists:
			# 如果不存在则创建目录
			print(path+' 创建成功')
			# 创建目录操作函数
			os.makedirs(path)
			return True
		else:
			# 如果目录存在则不创建，并提示目录已存在
			print(path+' 目录已存在')
			return False
	def delDir(self,srvId,appId):
		path=self.getPath(srvId,appId)
		shutil.rmtree(path)
	
	def getRoot(self):
		print(' ConfigParent root dir')
		return os.getcwd()
		
	def getPath(self,srvId,appId):
		root = self.getRoot()
		path = root+self.splitor+self.configFolder+self.splitor+str(srvId)+self.splitor+str(appId)
		return path
	
