from django.shortcuts import render

def trainer_dashboard(request):
    return render(request,'trainer.html')
    
def trainer_transcation(request):
    return render(request,'transaction.html')
