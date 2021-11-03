from django.urls import path
from . views import redeem,student_profile,student_home,student_dashboard
# from core.views import Profile
urlpatterns =[
    path('student-home',student_home,name='student-home'),
    path('redeem/',redeem,name='redeem'),
    path('student-profile/',student_profile,name='student-profile'),
    path('student_dashboard/',student_dashboard,name='student_dashboard'),
    ]