from django.shortcuts import render, redirect
from .forms import RegisterForm , LoginForm
from django.contrib.auth import login , authenticate


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks')

    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('tasks')
                else:
                    return redirect('banned')
        else:
            form.add_error(None, "Неверное имя пользователя или пароль")
    else:
        form = LoginForm()
    
    context = {
        'form':form
    }
    return render(request, 'account/login.html', context)