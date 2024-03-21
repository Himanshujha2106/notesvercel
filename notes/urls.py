from django.contrib import admin
from django.urls import path,include
from backend.views import user_input_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
]
