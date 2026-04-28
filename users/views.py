from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserUpdateForm

# Create your views here.
def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'users/signup.html', context)

def profile(request):
    form = UserUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'users/profile.html', context)

def logoutconfirm(request):
    return render(request, 'users/logoutconfirm.html')