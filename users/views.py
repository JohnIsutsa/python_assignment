from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User not found!")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        
        return render(request, "welcome.html")
    
    return render(request, "auth/login.html")


# def register(request):
#     return JsonResponse({
#         "id": 12,
#         "email": "johnisutsa@gmail.com",
#         "phone_number": "233554707890",
#         "auth_token": "ajkbfajkvbabfibvie23240nfo2",
#     })

def template_ninja(request):
    return render(request, "ninja.html") 


# def login_user(request):
#     if(request.method == "POST"):
#         login()

def register(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, password, email)

        # message = ''

        # try: 
        #     us = User.objects.get(email = email)
        #     message = 'This email already exists.'
        # except User.DoesNotExist:
        #     user = User.objects.create_user(username, password, email)

    
    return render(request, "auth/register.html")