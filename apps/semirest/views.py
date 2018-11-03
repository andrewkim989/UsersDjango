from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import *

def users(request):
    all_users = {
        "users": User.objects.all()
    }
    return render (request, "user.html", all_users)

def add(request):
    return render (request, "new.html")

def add_process(request, methods = ['POST']):
    errors = User.objects.add_validate(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')
    else:
        User.objects.create(first_name = request.POST['first_name'],
        last_name = request.POST['last_name'], email = request.POST['email'])
    
    return redirect("/users")

def show(request, num):
    user = {
        "user": User.objects.get(id = num)
    }
    return render (request, "show.html", user)

def edit(request, num):
    user = {
        "user": User.objects.get(id = num)
    }
    return render (request, "edit.html", user)

def edit_process(request, num):
    user = User.objects.get(id = num)

    errors = User.objects.edit_validate(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/' + num + '/edit')
    if request.method == 'POST':

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

    return redirect("/users")

def delete(request, num):
    User.objects.get(id = num).delete()
    return redirect("/users")
