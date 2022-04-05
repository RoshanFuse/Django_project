from django.shortcuts import render,HttpResponseRedirect
from app2.forms import ShowData
from .models import Data
from django.contrib import messages


# Create your views here.
def home(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      sh = ShowData(request.POST,request.FILES)
      if sh.is_valid():
        sh.save()
    sh = ShowData()
    obj = Data.objects.all()
    return render (request,'app2/home.html', {'nam':sh,'pic':obj})
  else:
    return HttpResponseRedirect('/login/')
  
  
def delete(request,id):
    ak = Data.objects.get(id=id)
    ak.delete()
    return HttpResponseRedirect('/home/')
  
def update(request,id):
  if request.method == "POST":
    pi = Data.objects.get(pk=id)
    she = ShowData(request.POST,request.FILES,instance=pi)
    if she.is_valid():
      she.save()
      messages.success(request,"Data update succesfully!!!!!!!")
  else:
    pi = Data.objects.get(pk=id)
    she = ShowData(instance = pi)
  return render(request,'app2/update.html',{'deta':she})
  