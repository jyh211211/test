from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from .models import User

# Create your views here.

def index(request):
    return render(request, 'acc/index.html')

def userlogin(request):
    un=request.POST.get('uname')
    up=request.POST.get('upass')
    check=authenticate(username=un,password=up)
    if check:
        login(request, check)
        return redirect('acc:index')
    return render(request, 'acc/login.html')

def userlogout(request):
    logout(request)
    return redirect('acc:index')

def signup(request):
    r=request.POST
    un=r.get('uname')
    upw=r.get('upass')
    ue=r.get('umail')
    upic=request.FILES.get('upic')
    if request.method=='POST':
        User.objects.create_user(username=un,password=upw,email=ue,pic=upic)
        return redirect('acc:login')
    return render(request, 'acc/signup.html')