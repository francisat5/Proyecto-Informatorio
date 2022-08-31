from django.urls import path 

from . import views

app_name = "registrarse"

urlpatterns = [

    path('registrar/', views.registrar.as_view(), name="registrar"),

]