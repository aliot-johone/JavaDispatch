# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
from django.views.decorators.csrf import csrf_exempt
import traceback
from DeployConfig.ConfigParent import ConfigParent

class  WindowsConfig(ConfigParent)  :
	
	splitor = '\\'

