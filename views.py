from opcode import hasname
from weakref import ref
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Drinks,customer,order,courses,photo


# Create your views here.


def memb(request):
    return render(request,'app/first.html')

def membm(request):
    return render(request,'app/second.html')

def add(request):
    if request.method=="POST":
        t=request.POST["tea"]
        c=request.POST["coffee"]
        s=request.POST["snaks"]
        d=request.POST["juice"]

        obj=Drinks(tea=t,coffee=c,snaks=s,juice=d)
        obj.save()
        return render(request,'app/success.html')
    return render(request,'app/items.html')
    

def succ(request):
    return render(request,'app/success.html')

def curd(request):
    return render(request,'app/empregister.html')

def index(request):
    return render(request,'app/index.html')



def customer_v(request):
    if request.method == "POST":
        cname = request.POST['cname']
        number = request.POST['number']
        mail = request.POST['mail']
        obj = customer(cname=cname, number=number, mail=mail)  
        obj.save()
        return render(request, 'app/index.html')  
     
    return render(request, 'app/customer.html')

def read_customer(request):
    data = customer.objects.all()  # fetches all records from the database
    return render(request, 'app/read.html', {'data': data})


def cus_update(request, pk):
    obj = customer.objects.get(pk=pk)
    if request.method == "POST":
        obj.cname = request.POST['cname']
        obj.number = request.POST['number']
        obj.mail = request.POST['mail']
        obj.save()  # ✅ now save will store updated values

        return redirect('read_c')  # use redirect to avoid resubmission
    return render(request, 'app/update.html', {'customer': obj})


#going to do crud for order
#first insert the data
def orders(request):
    if request.method=="POST":
        cs=request.POST['csname']
        pro=request.POST['product']
        pr=request.POST['price']
        ad=request.POST['add']
        obj=order(csname=cs, product=pro, price=pr, add=ad)
        obj.save()
        return redirect('ordetails')
    return render(request,'app/order.html')

#now we wants to do the reading the data from database
def read(request):
    data=order.objects.all()
    return render(request,'app/orread.html',{'da':data})
#now we are go to update the existing record

def orupdate(request, pk):
    da = get_object_or_404(order, pk=pk)  # ✅ move outside to use in both GET & POST
    if request.method == "POST":
        da.csname = request.POST['csname']
        da.product = request.POST['product']
        da.price = request.POST['price']
        da.add = request.POST['add']
        da.save()
        return redirect('ordetails')  # ✅ use the name of your view, not the request
    return render(request, 'app/oupdate.html', {'read': da})

def delete(request,pk):
    de=get_object_or_404(order, pk=pk)
    if request.method=="POST":
        de.delete()
        return redirect('ordetails')
    return render(request,'app/delet.html')

def course(request):
    if request.method=="POST":
        c=request.POST['crname']
        prr=request.POST['price']
        du=request.POST['duration']
        do=request.POST['doj']
        da = courses(crname=c ,price=prr ,duration=du,doj=do)
        da.save()
        return redirect('courseread')
    return render(request,'app/courseins.html')

def reead(request):
    d=courses.objects.all()
    return render(request,'app/courread.html',{'da':d})

def curupdate(request,pk):
    if request.method=="POST":
        d=get_object_or_404(courses,pk=pk)
        d.crname=request.POST['crname']
        d.price=request.POST['price']
        d.duration=request.POST['duration']
        d.doj=request.POST['doj']
        d.save()
        return redirect('courseread')
    return render(request,'app/crupdate.html')

def deletee(request,pk):
    if request.method=="POST":
        d=get_object_or_404(courses,pk=pk)
        d.delete()
        return redirect('courseread')
    return render(request,'app/dele.html')

def imupl(request):
    if request.method=="POST":
        n=request.POST['name']
        im=request.FILES['img']
        f=photo(name=n ,img=im)
        f.save()
        return redirect('courseread')
    return render(request,'app/imcre.html')