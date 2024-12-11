from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Перевірка автентифікації користувача
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('register')
            else:
                form.add_error(None, 'Невірний email або пароль')
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')








