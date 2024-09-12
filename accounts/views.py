from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messages

def login_page(request):
    if request.user.is_authenticated:
        return redirect("repoter_news")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect('repoter_news')
        else:
            return redirect('login_page')
    return render(request, "accounts/login.html")

"""
logout page
"""
@login_required(login_url='home_page')
def repoter_logout(request):
    try:
        logout(request)
    except Exception as e:
        messages.error(request, "error while logout")
    return redirect("home_page")