from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.myfun,name='home'),
    path('test',views.testfun,name='test'),
    path('test1',views.test1fun,name='test1'),

]
