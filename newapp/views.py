from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfun(request):
    return HttpResponse('hiiiiiii')
def testfun(request):
    return render(request,'index.html')
def test1fun(request):
    return render(request,'assignment1.html')
def test2fun(request):
    return render(request,'assignment2.html')