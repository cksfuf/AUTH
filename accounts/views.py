from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signup')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # 로그인하지 않고 페이지 이동했다면 로그인시키고 이동하려는 페이지로 이동시키기.
            next_url = request.GET.get('next')
            # next 인자에 url이 없을 경우 -> None or 'articles:index' (없으면 'articles:index'로 이동)(단축평가)
            # next 인자에 url이 있을 경우 -> '/articles/1/' or 'articles:index' (있으면 /articles/1/'로 이동)(단축평가)
            return redirect(next_url or 'articles:index')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)

    return redirect('accounts:login')