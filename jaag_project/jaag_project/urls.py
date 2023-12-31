"""
URL configuration for jaag_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trellaapp import views 



# ###GET AND POST METHOD
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home),
#     path('product', views.product),
#     path('',views.register),
#     path('result',views.result),
# ]


#####STATIC FILES  FOR IAMGE

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.image),
#     ] 

# BOOTSTRAP
# urlpatterns = [
#      path('admin/', admin.site.urls),
#      path('',views.bootstrap),
#      ]


## CRUD:
urlpatterns = [
          path('admin/', admin.site.urls),
          path('',views.crud,name="crud"),
          path('adddata',views.adddata,name="adddata"),
          path('updatedata/<int:id>',views.updatedata,name="updatedata"),
           path('deletadata/<int:id>',views.deletedata,name="deletedata"),
 ]
