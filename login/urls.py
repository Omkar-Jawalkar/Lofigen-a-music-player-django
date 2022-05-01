from django.urls import path, include
from .views import adminlogin, userlogin

urlpatterns = [
    path('adminlogin/', adminlogin, name="adminlogin"),
    path('userlogin/', userlogin, name="userlogin"),

]
