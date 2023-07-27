from django.shortcuts import render,redirect
from django.http import HttpResponse
from pathlib import Path 
from .models import data
# import os


# # Create your views here.

# BASE_DIR = Path(__file__).resolve().parent.parent



# def home(request):

#     # result=os.path.join(BASE_DIR,"template")
#     # print(result)
#     # return render(request,"home.html", {'name':'gotam'})
#      return render(request,"home.html")

# def product(request):
#      mobile=int(request.GET["mobile"])
#      keyboard=int(request.GET["keyboard"])
#      monitor=int(request.GET["monitor"])
#      price=mobile+keyboard+monitor
#      return render(request,'results.html',{'price':price,})




# ###HOW USE GET METHOD AND POST METHOD 
# def register(request):
#      return render(request,'register.html')

# def result(request):
#      name=request.POST['name']
#      password=request.POST['password']
#      address=request.POST['address']
#      email=request.POST['email']
#      return render(request,'output.html',{'name':name,'password':password,'address':address,'email':email})






##HOW USE STATIC

# def image(request):
#     return render(request,'image.html')


##BOOTSTRAP 
# def bootstrap(request):
#     return render(request,'bootstrap.html')





### HOW TO USE CRUD :

def crud(request): #127.0.0.1:8000/  home page
    mydata=data.objects.all()
    if(mydata!=""):
        return render(request,"crud.html",{'datas':mydata})
    else:
        return render(request,"crud.html")




def adddata(request): # if i summit after filling all detalis in html then summit the summit botton the ACTION  will be come this lines  
      if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        obj=data()
        obj.name=name
        obj.age=age
        obj.address=address
        obj.contact=contact
        obj.mail=mail
        obj.save()
        mydata=data.objects.all()
        return redirect('crud') #127.0.0.1:8000/  home page
      return render(request,"crud.html")


def updatedata(request,id): #127.0.0.1:8000/updatedate/id
    mydata=data.objects.get(id=id)
    print(mydata)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        mydata.name=name
        mydata.age=age
        mydata.address=address
        mydata.contact=contact
        mydata.mail=mail
        mydata.save()
        return redirect('crud')
    return render(request,"update.html",{'data':mydata})


def deletedata(request,id): #127.0.0.1:8000/updatedate/id
     mydata=data.objects.get(id=id) #object(2) it will delete the id based 
     mydata.delete()
     return redirect('crud')