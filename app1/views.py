from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from app1.forms import SignUp
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'app1/index.html')

def Signup(request):
    if request.method == "POST":
        fm = SignUp(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"sign_up succesfully!!!!!!!")
            return HttpResponseRedirect('/login/')
    else:
      fm = SignUp()
    return render(request,'app1/signup.html',{'form':fm})

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            at = AuthenticationForm(request.POST, data=request.POST) 
            if at.is_valid():
                usn = at.cleaned_data['username']
                pas = at.cleaned_data['password']
                user = authenticate(username=usn,password=pas)
                if user is not None:
                    login(request, user)
                    messages.success(request,"login succesfully!!!!!!!")
                    return HttpResponseRedirect('/home/')
        else:      
            at = AuthenticationForm()
        return render(request,'app1/login.html',{'form':at})
    else:
       return HttpResponseRedirect('/home/')
   
def logout_user(request):
    logout(request)
    messages.success(request,"logout succesfully!!!!!!!")
    return HttpResponseRedirect('/login/')
        
   
