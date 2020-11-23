from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from auth_user.forms import UserForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username') # name attribute of input tag
        password = request.POST.get('password')

        user_auth = authenticate(request, username=username, password=password)
        if user_auth:
            login(request, user_auth)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'auth/login.html')


def register_page(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(pk=int(request.POST['groups']))
            user.groups.add(user_group)
            return redirect('login')
        else:
            print('Registration form is not valid')
            return redirect('register')
    
    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)


@login_required(login_url='/auth/login')
def logout_page(request):
    logout(request)
    return redirect('login')
