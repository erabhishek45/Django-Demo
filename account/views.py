from django.shortcuts import render



def home(request):
	return render(request, 'account/home.html')

def register(request):
	return render(request, 'account/register.html')


def login(request):
	return render(request, 'account/login.html')


def logout(request):
	return render(request, 'account/logout.html')


def reset_password(request):
	return render(request, 'account/reset.html')
