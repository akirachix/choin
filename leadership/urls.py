from django.urls import path
from . views import profile_upload, reward
urlpatterns =[
    path('upload/',profile_upload,name='upload'),
    path('reward/', reward, name='reward')

]