from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render,redirect
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, "home.html")
    def post(self,request):
        l=request.POST.get("login")
        p=request.POST.get("password")
        userlar=authenticate(request, username=l, password=p)
        if userlar is None:
            return redirect("login")
        login(request, userlar)
        return redirect("bolim")
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("login")

