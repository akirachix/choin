from django.urls import path
from . views import *

urlpatterns=[
    path('',index,name='index'),
    path('/profile',Profile,name='user_profile')

    ]