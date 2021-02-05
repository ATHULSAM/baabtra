from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.myfun,name='home'),
    path('test',views.testfun,name="test"),
    path('test1',views.test1fun,name="test1"),
    path('test2',views.test2fun,name="test2"),
    path('test3',views.test3fun,name="test3"),
    path('sample',views.samplefun),
    path('sample1',views.samfun,name="sample1"),
    path('form',views.formfun,name="form"),
    path('fb',views.fbfun,name="fb"),
    path('sample2',views.sample2fun,name="sample2"),
    
    

]
