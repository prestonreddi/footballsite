from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

"""
Handles registration for the user.
"""
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
