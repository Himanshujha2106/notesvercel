from django.shortcuts import render
from .forms import UserCredentialsForm
from django.http import HttpResponse
from frontend.models import UserCredentials

def user_input_view(request):
    if request.method == 'POST':
        form = UserCredentialsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'success.html')  # Redirect to a success page or another URL
    else:
        form = UserCredentialsForm()


    # ans=UserCredentials.objects.get(username='chirag')
    return render(request, 'user_input.html', {'form': form})

def index(request):
    return render(request,'index.html')

def passcheck(request):
    key=request.POST.get('password')

    if UserCredentials.objects.filter(password=key).exists():
        note=UserCredentials.objects.get(password=key)
        return render(request,'success.html',{"body":note.notes,"result":1})
    else:
        return render(request,'success.html',{"name":"none","result":0})
