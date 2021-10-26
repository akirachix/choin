from django.urls import path
from . views import redeem_item
urlpatterns =[
    path('redeem/',redeem_item,name='redeem_item')

    ]