from django.urls import path
from . import views

urlpatterns = [
    path('usercreation', views.user_input_view,name="createuser"),
    path('', views.index,name="index"),
    path('passcheck', views.passcheck,name="password"),
]
