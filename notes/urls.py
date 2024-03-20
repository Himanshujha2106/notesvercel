from django.contrib import admin
from django.urls import path
from backend.views import user_input_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_input_view, name='user_input'),
]
