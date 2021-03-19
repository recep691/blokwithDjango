from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data
        password = form.cleaned_data.get("password")
        newuser = User(username =username)
        newuser.set_password(password)
        newuser.save()
        login(request,newuser)
        messages.success(request,"basariyla giris yaptiniz")
        return redirect("index")
    context = {
        "form" : form
    }
        
    return render(request,"register.html",context)
    


    """
    POST 1. YOL
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data
            password = form.cleaned_data.get("password")
            newuser = User(username =username)
            newuser.set_password(password)
            newuser.save()
            login(request,newuser)
            return redirect("index")
        context = {
            "form" : form
        }
        return render(request,"register.html",context)
    else:
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request,"register.html",context)
        """


    """
    form = RegisterForm()
    context = {
        "form" : form
    }

    return render(request,"register.html",context)
    """
def loginuser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid() :
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,"hatali parola yada kullanici adi")
            return render(request,"login.html",context)
        login(request,user)
        messages.success(request,"basarili giris")
        return redirect("index")
    
    return render(request,"login.html",context)

    

def logoutuser(request):
    logout(request)
    messages.success(request,"cikis tyapildi")
    return render(request,"index.html")