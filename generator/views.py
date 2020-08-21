from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def signUp(request):
    return render(request, 'generator/signup.html')

def password(request):
    finalPass = ''
    requirments = list()
    
    # get the Values of The Choicesb
    if request.GET.get('uppercase'):
        requirments.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('lowercase'):
        requirments.extend(list('abcdefghijklmnopqrstuvwxyz'))    
    if request.GET.get('symbols'):
        requirments.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        requirments.extend(list('0123456789'))
    
    length = int(request.GET.get('length'))
    
    for x in range(length):
        try:
            finalPass += random.choice(requirments)
        except:
            print('Hello Friend')

    return render(request, 'generator/password.html', {'password': finalPass })   

def about(request):
    return render(request, 'generator/about.html')
