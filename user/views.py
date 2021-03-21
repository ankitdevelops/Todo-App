from django.contrib.auth.forms import UserCreationForm
from django.db.models.query import RawQuerySet
from django.shortcuts import redirect, render
from . forms import userRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == "POST":
        form = userRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            form.save()
            return redirect('login')
    else:
        form = userRegisterForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            return redirect('tasks')
    
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    data = {
        'p_form':p_form,
        'u_form':u_form,
    }
    return render(request, 'profile.html', data)

def logout_user(request):
    logout(request)
    return redirect('login')