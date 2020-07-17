from django.shortcuts import render, HttpResponse
from .forms import RegistrationForm
# Create your views here.

def accounts(request):
	"""Displays options for registration/login on landing"""
	return render(request, 'accounts/accounts.html')

def register(request):
	"""Registration of new accounts"""
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = RegistrationForm()
	return render(request, 'accounts/register.html', {'form': form})

def login(request):
	"""Logs into existing accounts"""
	return render(request, 'accounts/login.html')

def profile(request):
	"""Display info about certain account"""
	return HttpResponse('View profile here...')