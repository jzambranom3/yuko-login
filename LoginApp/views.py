from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError


def Login(request):
	return render(request, 'login.html', {'estado': 0})


def Autenticacion(request):
	try:
		username = request.POST['usuario']
		password = request.POST['clave']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/index/')
		else:
			return render(request, 'login.html', {'estado': 1})
	except Exception as e:
		return render(request, 'login.html', {'estado': 0})
	
def Logout(request):
	try:
		logout(request)
	except Exception as e:
		pass
	finally:
		return render(request, 'login.html', {'estado': 0})

@login_required(login_url='/')
def Index(request):
	return render(request, 'index.html', {'username': request.user.username})

def Register(request):
	try:
		if request.method == 'POST':
			user = User.objects.create_user(username = request.POST['usuario'], password = request.POST['clave'], email = request.POST['correo'])
			return render(request, 'register.html', {'estado': 1})
		return render(request, 'register.html', {'estado': 3})
	except IntegrityError as e:
		return render(request, 'register.html', {'estado': 2})
	except Exception as e:
		return render(request, 'register.html', {'estado': 0})
	