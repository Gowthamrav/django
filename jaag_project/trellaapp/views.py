from django.shortcuts import render
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

def crud(request):
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
    return render(request,"crud.html")