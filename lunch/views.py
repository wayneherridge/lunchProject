from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm

import lunch
# Create your views here.
from .forms import LunchItemForm
from .models import LunchItem

# CRUD - Create, Read, Update, Delete

# Home View
def home_view(request):
    return render(request, 'lunch/home.html')

# Create
def lunch_create_view(request):
    form = LunchItemForm()
    if request.method == 'POST':
        form = LunchItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lunch_list')
    return render(request, 'lunch/lunch_form.html', {'form': form})

# Read
def lunch_list_view(request):
    lunches = LunchItem.objects.filter(lunch_date=datetime.today())
    return render(request, 'lunch/lunch_list.html', {'lunches': lunches})

# Update
def lunch_update_view(request, lunch_id):
    lunch = LunchItem.objects.get(lunch_item_id=lunch_id)
    form = LunchItemForm(instance=lunch)
    if request.method == 'POST':
        form = LunchItemForm(request.POST, instance=lunch)
        if form.is_valid():
            form.save()
            return redirect('lunch_list')
    return render(request, 'lunch/lunch_form.html', {'form': form})

# Delete
def lunch_delete_view(request, lunch_id):
    lunch = LunchItem.objects.get(lunch_item_id=lunch_id)
    if request.method == 'POST':
        lunch.delete()
        return redirect('lunch_list')
    return render(request, 'lunch/lunch_confirm_delete.html', {'lunch': lunch})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid credentials"
    return render(request, 'accounts/login.html', {'error': error_message})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')

@login_required
def lunch_view(request):
    return render(request, 'lunch/lunch_list.html')

class protected_view(LoginRequiredMixin, View):
    login_url = '/login/'
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'lunch/lunch_list.html')

