from django.shortcuts import render, redirect
from .models import Apples
from .forms import Apple
from django.http import HttpResponse
def invalid(request):
    return render(request,"invalid.html")
def index(request):
    apple = Apples.objects.first()
    number = apple.number if apple else 0
    return render(request, "index.html", {'number': number})

def add(request):
    form = Apple()
    apple = Apples.objects.first()
    number = apple.number if apple else 0
    return render(request, "add.html", {"form": form, "number": number})

def addhandle(request):
    if request.method == "POST":
        form = Apple(request.POST)
        if form.is_valid():
            number = form.cleaned_data["number"]
            apple = Apples.objects.first()

            if not apple:
                apple = Apples(number=number)
            elif number<0 or number>100:
                return redirect('invalid')
            else:
                apple.number += number

            apple.save()

            # Redirect to a new URL for the thanks page
            return redirect('thanks')  # Ensure this URL is defined in your urls.py
    
    return redirect('add')  # Redirect back to add if form is invalid or not POST
def edithandle(request):
    if request.method == "POST":
        form = Apple(request.POST)
        if form.is_valid():
            number = form.cleaned_data["number"]
            apple = Apples.objects.first()

            if not apple:
                apple = Apples(number=number)
            elif number<0 or number>100:
                return redirect('invalid')
            else:
                apple.number -= number

            apple.save()


            return redirect('thanks') 
    
    return redirect('edit') 

def deletehandle(request):
    apple = Apples.objects.first() 
    apple.number=0 
    apple.save()
    return redirect('thanks')  
    
def edit(request):
    apple = Apples.objects.first()
    number = apple.number if apple else 0
    form = Apple()
    return render(request, "edit.html",{"form":form,"number":number})

def delete(request):
    apple = Apples.objects.first()
    number = apple.number if apple else 0
    form = Apple()
    return render(request, "delete.html",{"form":form,"number":number})

def thanks(request):
    return render(request, "thanks.html")
