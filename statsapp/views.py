from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Ombor
from asosiy.models import *

class StatsView(View):
    def get(self,request):
        o=Ombor.objects.get(user=request.user)
        s=Stats.objects.filter(ombor=o)
        m=Mahsulot.objects.filter(ombor=o)
        c=Client.objects.filter(ombor=o)
        return render(request, "stats.html", {"stats":s, "mahsulot":m, "client":c})
    def post(self,request):
        o = Ombor.objects.get(user=request.user)
        m=Mahsulot.objects.get(id=request.POST.get("mah"))
        c=Client.objects.get(id=request.POST.get("c"))
        f=int(request.POST.get("u"))-(int(m.kelgan_narx)*int(request.POST.get("m")))
        Stats.objects.create(
            umumiy=request.POST.get("u"),
            tolandi=request.POST.get("t"),
            miqdor=request.POST.get("m"),
            nasiya=request.POST.get("n"),
            mahsulot=m,
            client=c,
            foyda=f,
            ombor=o,
        )
        m.miqdor-=int(request.POST.get("m"))
        m.save()
        c.qarz+=int(request.POST.get("n"))
        c.save()
        return redirect("stats")