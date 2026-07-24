from django.shortcuts import render, redirect
from .models import Student
from .temp import FormView
import pandas as pd
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def admin_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, data = req.POST)
        if form.is_valid():
            login(req, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(req, 'login.html', {'form':form})

def admin_signup(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(req, 'signup.html', {'form':form})

@login_required(login_url='login')
def admin_logout(req):
    logout(req)
    return redirect('login')

@login_required(login_url='login')
def home(req):
    data = Student.objects.all()
    return render(req,'home.html',{'d':data})

@login_required(login_url='login')
def create(req):
    if req.method == 'POST':
        form = FormView(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = FormView()

    return render(req, 'create.html', {'form':form})

@login_required(login_url='login')
def update(req, id):
    obj = Student.objects.get(id=id)
    if req.method == 'POST':
        form = FormView(req.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = FormView(instance=obj)

    return render(req, 'update.html', {'form':form})

@login_required(login_url='login')
def delete(req, id):
    obj = Student.objects.get(id = id)
    obj.delete()
    return redirect('home')

@login_required(login_url='login')
def data_to_csv(req):
    data = Student.objects.all().values()
    df = pd.DataFrame(data)
    df.to_csv("C:/Users/talav/Downloads/Student_data.csv",index=False,encoding='utf-8')
    return redirect('home')