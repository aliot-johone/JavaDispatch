from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from account.models import Account

# Create your views here.

def login(request):
	context= {}
	print('login')
	return render(request, 'login.html', context)
	
@csrf_exempt
def verify(request):
	request.encoding='utf-8'
	context = {}
	account = request.POST['account']
	passwd = request.POST['passwd']
	print('account')
	print('passwd')
	try:
		obj = Account.objects.get(account=account)

		if(passwd==obj.passwd): 
			return render(request, 'index.html', context)
	except BaseException:
		context['msg']='login_error'
	
	context['msg']='login_error'
	return render(request, 'login.html', context)


@csrf_exempt
def index(request):
	request.encoding='utf-8'
	context = {}
	context['hello']='Hello World!'
	print('12')
	return render(request, 'accountList.html', context)