from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        data = {}
        return render(request, "profile.html", data)
    else:
        return redirect("auth_login")