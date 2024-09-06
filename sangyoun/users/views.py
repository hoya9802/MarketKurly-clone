from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from users.models import User
import datetime
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=username, email=email, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")    

    return render(request, "users/login.html")



def logout_view(request):
    logout(request)
    return redirect("users:login")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        gender = request.POST["gender"]
        birth = request.POST["birth"]
        try:
         birth = datetime.datetime.strptime(birth, "%Y-%m-%d").date()
        except ValueError:
        # 날짜 형식이 맞지 않을 때 처리
            pass
        
        users = User.objects.create_user(username,  email, password,)
        users.last_name = lastname
        users.first_name = firstname
        users.gender = gender
        users.birth = birth
        users.save()
        return redirect("users:login")
    return render(request, "users/signup.html")

