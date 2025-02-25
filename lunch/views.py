from datetime import datetime

from django.shortcuts import render, redirect

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
