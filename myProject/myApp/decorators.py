from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user (view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('landingpage')
        else:
            return view(request, *args, **kwargs)
    return wrapper  

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed in here!")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):

        group = None

        if request.user.groups.exists():
                group = request.user.groups.all()[0].name

        if group == 'alumni':
            return redirect('homepage')
        
        if group == 'admin':
            return redirect('adminhomepage')
        
    return wrapper_function
