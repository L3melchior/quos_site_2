from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import sqlite3
from django.views.decorators.csrf import csrf_exempt
import math
import itertools
import random
import datetime

def gen_request_qr_code():
    alp = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','0','2','3','4','5','6','7','8','9']

    l = []
    for i in range(16):
        n = random.choice(alp)
        l.append(n)

    def chunks(lst, chunk_size):
        for i in range(0, len(lst), chunk_size):
            yield lst[i:i + chunk_size]

    chunks_list = list(chunks(l, 4))

    code_request = ""
    for i in chunks_list:
        for n in i:
            code_request = code_request + str(n)
        code_request = code_request + "-"
    code_request = code_request[:-1]

    print(code_request)
    return(code_request)

# Create your views here.
def partition(l, size):
    for i in range(0, len(l), size):
        yield list(itertools.islice(l, i, i + size))

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")    
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print("/////////////////////////////")
                print(request.user.profile.students.all().exists())
                print("/////////////////////////////")
                if request.user.profile.students.all().exists() == False:
                    return redirect('home')
                elif request.user.profile.students.all().exists():
                    return redirect('home')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        pass
    return render(request, 'account/login.html') 

def get_qr(request):
    context = None
    user = request.user.profile
    code_request = gen_request_qr_code()
    get_qr = RequestQR.objects.create(code_request=code_request, owner_request=user.name_user, child_owner=user.students, child_class=user.students_class)
    context ={
        "qr" : code_request
    }
    return render(request, 'main/get_qr.html', context) 

def home(request):
    context = None
    access = request.user.profile.access
    if request.user.profile.access == "Учитель":
        user_class = request.user.profile.students_class
        requests = RequestQR.objects.filter(child_class = user_class, entered_at = str, closed_at = None)
        context = {
        'requests': requests,
        'access' : access,
        'class' : user_class
        }
    else:
        context = {
            'access': access 
        }
    return render(request, 'main/home.html', context)

def scan_qr(request):
    if request.method == 'POST':
        show = request.COOKIES['data_dj']
        if RequestQR.objects.filter(code_request = show,  entered_at = None, closed_at = None).exists():
            requests = RequestQR.objects.get(code_reques = show)
            requests.entered_at = str(datetime.now)
            requests.save()
        elif RequestQR.objects.filter(code_request = show,  entered_at = str, closed_at = None).exists():
            requests = RequestQR.objects.get(code_reques = show)
            requests.closed_at = str(datetime.now)
            requests.save() 
        else:
            redirect("error_double_use")
    return render(request, 'main/scan_qr.html')

def error_double_use(request):
    return HttpResponse("Пользователь пытается зайти дважды!")

from rest_framework import generics
from Users.models import RequestQR
from Users.serializers import RequestQRSerializer

class RequestQRList(generics.ListCreateAPIView):
    queryset = RequestQR.objects.all()
    serializer_class = RequestQRSerializer

class RequestQRDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestQR.objects.all()
    serializer_class = RequestQRSerializer