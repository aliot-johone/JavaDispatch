# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import os
import shutil
import traceback


class  JdFileConfig:
	
	def getRoot(self):
		folder = "upload";
		print('jd file Config root dir')
		path = os.path.join(os.getcwd(), folder)
		return path
	
	def getFilePath(self,name):
		root = self.getRoot()
		return os.path.join(root, name)
	
	def getNewName(self,name):
		gname = self.genName()
		ext = self.getExt(name)
		tmp_file_name = '%s%s' %(gname,ext)
		return tmp_file_name
		
	def genName(self):
		tm =  datetime.datetime.now()
		TIMESTAMP="%Y%m%d%H%M%S"
		return tm.strftime(TIMESTAMP)
	
	def getExt(self,path):
		return os.path.splitext(path)[1]