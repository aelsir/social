from django.shortcuts import redirect, render
from django.urls import reverse

def prevent_registered_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'account/register_already.html')
        return view_func(request, *args, **kwargs)
    return wrapper