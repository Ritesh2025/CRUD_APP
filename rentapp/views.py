from django.shortcuts import render,redirect
from .models import Ritesh

# Create your views here.
def index(request):
    data=Ritesh.objects.all()
    print(data)
    context={"data":data}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def insertData(request):
    
    if request.method=="POST":
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        unit= request.POST.get('unit')
        bill= request.POST.get('bill')
        print(fname, lname, email, phone, unit, bill)
        query=Ritesh(fname=fname, lname=lname, email=email, phone=phone, unit=unit, bill=bill)
        query.save()
        return redirect("/")

    return render(request, "index.html")


def updateData(request, id):
    if request.method=="POST":
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        phone= request.POST['phone']
        unit= request.POST['unit']
        bill= request.POST['bill']
        edit=Ritesh.objects.get(id=id)
        edit.fname=fname
        edit.lname=lname
        edit.email=email
        edit.phone=phone
        edit.unit=unit
        edit.bill=bill
        edit.save()
        
        return redirect("/")
    
    d=Ritesh.objects.get(id=id)
    context={"d":d}
    return render(request, "edit.html",context)

def deleteData(request, id):
    d=Ritesh.objects.get(id=id)
    d.delete()
    return redirect("/")

    