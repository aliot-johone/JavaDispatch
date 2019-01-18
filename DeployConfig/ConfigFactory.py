# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import traceback
from DeployConfig.WindowsConfig import WindowsConfig
from  DeployConfig.LinuxConfig import LinuxConfig


class  ConfigFactory  :
	
	types=('windows','linux')
	
	def getConfig(self,tp):
		if tp == self.types[0]:
			return WindowsConfig()
		else:
			return LinuxConfig()
		
	
		
