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
def test3fun(request):
    return render(request,'assignment3.html')  
def samplefun(request):
    return render(request,'sample.html')  
def samfun(request):
    return render(request,'bs.html')    
def formfun(request):
    return render(request,'form.html')    
def fbfun(request):
    return render(request,'fb.html')  
def pjtfun(request):
    return render(request,'pjt.html')
def jsfun(request):
    return render(request,'js.html')    
def sample2fun(request):
    return render(request,'assignment5.html')      


