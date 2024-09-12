from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from users.models import User
import datetime
from django.contrib import messages
# Create your views here.

def login_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
    #    username = request.POST["username"]
    #    email = request.POST["email"]
    #    password = request.POST["password"]
        user = authenticate(username=username, email=email, password=password)
        print(user)
    #    print(email)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")
            messages.error(request, "로그인에 실패했습니다. 다시 시도하세요.")    

    return render(request, "users/login.html")



def logout_view(request):
    logout(request)
    messages.success(request, "성공적으로 로그아웃을 했습니다!!")
    return render(request, "users/logout.html")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username", "")
    #    username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        gender = request.POST["gender"]
        birth = request.POST["birth"]
        profile_image = request.FILES.get('profile_image')
        short_description = request.POST['short_description']

        try:
            birth = datetime.datetime.strptime(birth, "%Y-%m-%d").date()
        except ValueError:
        # 날짜 형식이 맞지 않을 때 처리
            return render(request, "users/signup.html", {"error": "Invalid birth date format."})
        
        users = User.objects.create_user(username,  email, password,)
        print(users)
        users.last_name = lastname
        users.first_name = firstname
        users.gender = gender
        users.birth = birth
        users.profile_image = profile_image
        
        users.short_description = short_description
        print(users)
        users.save()
        return redirect("users:login")
    return render(request, "users/signup.html")


def usersinfo_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, "users/usersinfo.html")
