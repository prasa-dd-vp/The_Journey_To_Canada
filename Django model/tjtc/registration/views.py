from django.http import JsonResponse
from django.shortcuts import render
from registration.models import User

# Create your views here.
def show_page(request):
    return render(request, 'registration/register.html')

def save_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        user = User.objects.create( name = name,
                                    age = age,
                                    gender = gender,
                                    email = email,
                                    phone = phone,
                                    password = password)   
        user.save()
        return JsonResponse({"success":True},status=200)
