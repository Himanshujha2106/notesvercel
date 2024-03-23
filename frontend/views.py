from django.shortcuts import render
from .forms import UserCredentialsForm
from django.http import HttpResponse
from frontend.models import UserCredentials

def user_input_view(request):
    if request.method == 'POST':
        form = UserCredentialsForm(request.POST)
        if form.is_valid():
            form.save()
            a="Registered succesfully"
            return render(request,'success.html',{"body":a})  # Redirect to a success page or another URL
    


    # ans=UserCredentials.objects.get(username='chirag')
    return render(request, 'user_input.html', {'form': form})

def index(request):
    return render(request,'index.html')

def passcheck(request):
    key=request.POST.get('password')
    a=UserCredentials.objects.filter(password=key).exists()
    if a:
        note=UserCredentials.objects.get(password=key)
        return render(request,'success.html',{"body":note.notes})
    else:
        a="wrong password,Try again"
        return render(request,'success.html',{"body":a})

