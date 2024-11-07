from multiprocessing import context
from operator import imod
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib import messages

from .models import Alumni
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import CreateUserForm

from .decorators import allowed_users, unauthenticated_user, admin_only


def landingpage(request):
    return render(request, 'base/landingpage.html')

@login_required(login_url='userlogin')
@admin_only
def adminhomepage(request):
    return render(request, 'base/adminhomepage.html')

@login_required(login_url='userlogin')
@admin_only
def homepage(request):
    return render(request, 'base/homepage.html')

# for sign up and login and logout

def usersignup(request):
    if request.user.is_authenticated:
        return redirect('landingpage')
    else: 
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='alumni')
                user.groups.add(group)

                messages.success(request, 'Account was created for ' + username)

                return redirect('userlogin')

        context = {'form': form}
        return render (request, 'base/signup.html', context)

@unauthenticated_user
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('landingpage')
        else:
            messages.info(request, 'Username or Password is incorrect!')

    context = {}
    return render (request, 'base/login.html', context)

def userconfirmlogout(request):
    return render (request, 'base/confirmlogout.html')

def userlogout(request):
    logout(request)
    return redirect('userlogin')


# end of sign up and log in

@login_required(login_url='userlogin')
def about(request):
    return render(request, 'base/about.html')

@login_required(login_url='userlogin')
def contact(request):
    return render(request, 'base/contact.html')

@login_required(login_url='userlogin')
def survey(request):
    return render(request, 'base/survey.html')

@login_required(login_url='userlogin')
def forgotpassword(request):
    return render(request, 'base/forgotpassword.html')

@login_required(login_url='userlogin')
def donation(request):
    return render (request, 'base/donation.html')

def alumni(request):
    alum=Alumni.objects.all()
    return render(request, 'base/alumni.html', {'alum': alum})