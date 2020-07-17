from django.shortcuts import render, HttpResponse

# Create your views here.

def accounts(request):
	"""Displays options for registration/login on landing"""
	return render(request, 'accounts/accounts.html')

def register(request):
	"""Registration of new accounts"""
	return render(request, 'accounts/register.html')

def login(request):
	"""Logs into existing accounts"""
	return render(request, 'accounts/login.html')

def profile(request):
	"""Display info about certain account"""
	return HttpResponse('View profile here...')