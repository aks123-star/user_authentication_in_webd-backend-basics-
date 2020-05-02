from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'a.html', {'topic': 'DJANGO', 'link':' http://127.0.0.1:8000/'} )

def profile(request):
    return render(request,'profile.html', { 'link':' http://127.0.0.1:8000/'} )

def expression(request):
    a = int(request.GET['text1'])
    b = int(request.GET['text2'])
    c = a+b
    return render(request,'expression.html', {'result':c, 'link':'http://127.0.0.1:8000/'})