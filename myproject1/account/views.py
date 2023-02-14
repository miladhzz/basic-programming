from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth.hashers import make_password


def signin(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admin/')
            print("not login")
    else:
        login_form = LoginForm()
    return render(request, "signin.html", {'form': login_form})


def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            form = signup_form.save(commit=False)
            form.password = make_password(signup_form.cleaned_data.get('password'))
            form.save()
            return redirect(reverse('signin'))
    else:
        signup_form = SignupForm()
    return render(request, "signup.html", {'form': signup_form})
