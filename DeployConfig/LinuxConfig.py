# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import traceback
from DeployConfig.ConfigParent import ConfigParent

class  LinuxConfig(ConfigParent)  :
	
	splitor = '/'

		
