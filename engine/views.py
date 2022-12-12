from django.http import HttpResponse
from django.shortcuts import render, redirect
from engine.forms import *

def register(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            return HttpResponse(f' {name}, поздравляю с регистрацией! <br> Указанные вами данные: <br> Имя - {name}, <br> Пароль - {password}, <br> Почта - {email}')
    userform = UserForm()
    return render(request, 'engine/register.html', context={'form': userform})


def login(request):
    if request.method == "POST":
        signform = SignForm(request.POST)
        if signform.is_valid():
            name = signform.cleaned_data['name']
            password = signform.cleaned_data['password']
            if name == 'User1' and password == '12345678':
                return HttpResponse('Поздравляем с успешным входом')
            else:
                return redirect(register)
    signform = SignForm()
    return render(request, 'engine/login.html', context={'form': signform})