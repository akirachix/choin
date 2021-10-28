from django.urls import path
from . views import trainer_dashboard,trainer_transcation
urlpatterns =[
    path('trainer_dashboard/',trainer_dashboard,name='trainer_dashboard'),
    path('trainer_transaction/',trainer_transcation,name="transaction.html")

    ]