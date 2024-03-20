from django.shortcuts import render, redirect
from .forms import UserCredentialsForm

def user_input_view(request):
    if request.method == 'POST':
        form = UserCredentialsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another URL
    else:
        form = UserCredentialsForm()
    return render(request, 'backend/user_input.html', {'form': form})
