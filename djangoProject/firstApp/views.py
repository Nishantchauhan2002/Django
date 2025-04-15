from django.shortcuts import render
from .models import userData

# Create your views here.

def allItems(request):
    users = userData.objects.all()
    print(users)
    return render(request,'firstApp/all_chai.html',{'users':users})
