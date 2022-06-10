from django.shortcuts import render,redirect
from django.views import View

from .models import *
from userapp.models import Ombor


class MahsulotView(View):
    def get(self,request):
        o=Ombor.objects.get(user=request.user)
        m=Mahsulot.objects.filter(ombor=o)
        return render(request, "products.html", {"mahsulot":m})
    def post(self,request):
        o = Ombor.objects.get(user=request.user)
        Mahsulot.objects.create(
            nom=request.POST.get("n"),
            brend=request.POST.get("b"),
            miqdor=request.POST.get("m"),
            kelgan_narx=request.POST.get("kn"),
            sotuv_narx=request.POST.get("sn"),
            ombor=o
        )
        return redirect("mahsulot")

class ClientView(View):
    def get(self,request):
        o=Ombor.objects.get(user=request.user)
        c=Client.objects.filter(ombor=o)
        return render(request, "clients.html", {"cl":c})
    def post(self,request):
        o = Ombor.objects.get(user=request.user)
        Client.objects.create(
            ism=request.POST.get("i"),
            tel=request.POST.get("t"),
            dokon=request.POST.get("d"),
            manzil=request.POST.get("m"),
            qarz=request.POST.get("q"),
            ombor=o
        )
        return redirect("client")
class BolimView(View):
    def get(self,request):
        return render(request, "bulimlar.html")


