from django.urls import path
from . import views

urlpatterns = [
    path('usercreation/', views.createuser,name="createuser"),
]
