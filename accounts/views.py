from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
from .forms import SignUpForm, LoginForm, EditForm


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']

            if password != password_confirm:
                form.add_error('password_confirm', 'Passwords do not match!')
            else:
                if User.objects.filter(email=email).exists():
                    form.add_error('email', 'Email is already in use!')
                if User.objects.filter(username=username).exists():
                    form.add_error('username', 'Username is already in use!')
                if not form.errors:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    login(request, user)
                    return redirect('/')
        else:
            form.add_error(None, 'Form is not valid!')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {"form": form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')


def user_edit(request):
    if not request.user.is_authenticated:
        return redirect('account:login')

    user = request.user

    if request.method == "POST":
        form = EditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditForm(instance=user)

    return render(request, 'accounts/edit.html', {'form': form})
