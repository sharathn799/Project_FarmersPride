from django.shortcuts import render, redirect
from account.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from cart.models import Cart

# Create your views here.

def register(request):
    if request.method == "POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/signin")
    else:
        fm=SignupForm()
    return render(request, "Register.html", {'form': fm})

def signin(request):
    if request.method == "POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request, user)
                return render(request, 'base.html', {'user':user})

    else:
        fm = AuthenticationForm()
    return render(request, "signin.html", {'form':fm})

def signout(request):
    logout(request)
    return redirect("signin/")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')

def home(request):
    return render(request, 'base.html')

def place_order(request):
    return render(request, "place_order.html")

def feedback(request):
    return render(request,'feedback.html')

def confirmation_view(request):
    return render(request, "confirmation.html")
