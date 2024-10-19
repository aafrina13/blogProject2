from django.shortcuts import render,redirect
from .models import Data
# Create your views here.
def login(request):
    return render(request,"login.html")
def result(request):
    username1=request.POST["username"]
    password1=request.POST["password"]

    obj=Data()
    obj.Username=username1
    obj.Password=password1
    obj.save()

    obj1=Data.objects.all()

    return render(request,'result.html',{'obj2':obj1})
    # return render(request,'result.html',{"username2":username1,"password2":password1})
def update(request,id):
    obj1=Data.objects.get(id=id)
    if request.method=='POST':
        username1 = request.POST["username"]
        password1 = request.POST["password"]

        obj1.Username = username1
        obj1.Password = password1
        obj1.save()

        return redirect('home')
    return render(request,"update.html",{'obj3':obj1})
def delete(request,id):
    obj1= Data.objects.get(id=id)
    if request.method=='POST':
        obj1.delete()
        return redirect('home')
    return render(request,'delete.html',{})