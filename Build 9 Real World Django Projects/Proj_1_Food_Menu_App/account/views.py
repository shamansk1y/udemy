from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistration, UserLogin
from django.contrib.auth import login, authenticate, logout


def logout_view(request):
    logout(request)
    return redirect('food:index')

def login_view(request):
    form = UserLogin(request.POST or None)
    next_get = request.GET.get('next')
    user_manager = request.user.groups.filter(name='manager').exists()
    user_auth = request.user.is_authenticated

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')
        return redirect(next_get or next_post or 'food:index')

    data = {
        'form': form,
        'user_manager': user_manager,
        'user_auth': user_auth,
    }
    return render(request, 'login.html', context=data)

def registration_view(request):
    form = UserRegistration(request.POST or None)
    user_manager = request.user.groups.filter(name='manager').exists()
    user_auth = request.user.is_authenticated

    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        data = {
            'form': form,
            'user_manager': user_manager,
            'user_auth': user_auth,
            'user': new_user,
        }
        return render(request, 'base.html', context=data)

    data = {
        'form': form,
        'user_manager': user_manager,
        'user_auth': user_auth,
    }
    return render(request, 'register.html', context=data)

@login_required
def profilepage(request):
    return render(request, 'profile.html')
