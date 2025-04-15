from django.shortcuts import render

# Create your views here.

def allItems(request):
    return render(request,'firstApp/all_chai.html')
