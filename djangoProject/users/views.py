from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import CustomUser
import json
from django.core.files.storage import default_storage
from datetime import datetime

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        required_fields = [
            'first_name', 'last_name', 'roll_number', 'gender', 'degree',
            'college', 'phone_number', 'email', 'address', 'password', 'dob'
        ]

        data = request.POST

        # Check if any field is missing
        for field in required_fields:
            if not data.get(field):
                return JsonResponse({'status': 'error', 'message': f'{field} is required'}, status=400)

        # Check for photo
        if 'photo' not in request.FILES:
            return JsonResponse({'status': 'error', 'message': 'photo is required'}, status=400)

        try:
            user = CustomUser.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                roll_number=data['roll_number'],
                gender=data['gender'],
                degree=data['degree'],
                college=data['college'],
                phone_number=data['phone_number'],
                email=data['email'],
                address=data['address'],
                password=data['password'],  # In production, use make_password
                dob=datetime.strptime(data['dob'], "%Y-%m-%d").date(),
                photo=request.FILES['photo']
            )
            return JsonResponse({'status': 'success', 'message': 'User created successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
