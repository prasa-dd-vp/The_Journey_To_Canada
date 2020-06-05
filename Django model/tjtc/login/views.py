from django.http import JsonResponse
from django.shortcuts import render
from registration.models import User

# Create your views here.
def show_page(request):
    return render(request, 'login/login.html')
