from django.shortcuts import render
from app1.forms import StudentForm,UserInfo
from app1.models import Userinfo

# Create your views here.

def student(request):
    form=StudentForm()
    if request.method =='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("invalid data")
        form=StudentForm()
    return render(request,'home.html',{'form':form})

def userinfo(request):
    form=UserInfo()
    if request.method =='POST':
        form=UserInfo(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            gender=form.cleaned_data['gender']
            contact=form.cleaned_data['contact']
            user=Userinfo(name=name,email=email,gender=gender,contact=contact)
            user.save()
            form=UserInfo()
        else:
            print("invalid data")
    return render(request,'home.html',{'form':form})
