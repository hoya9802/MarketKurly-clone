from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth import get_user_model
from users.forms import SignupForm
from django.contrib.auth.decorators import login_required


# Create your views here.
User = get_user_model()  # 현재 설정된 커스텀 사용자 모델을 가져옵니다.
User.objects.all()       # 이제 User 모델에 안전하게 접근할 수 있습니다.

def login_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
    #    username = request.POST["username"]
    #    email = request.POST["email"]
    #    password = request.POST["password"]
    #    user = authenticate(username=username, email=email, password=password)
    #    print(user)
    #    print(email)
        try:
            user=User.objects.get(username=username)
            if user.check_password(password):
                print("인증성공")
                login(request, user)
 #               print(login(request, user))
                return render(request, "users/userinfo.html")
            else:
                print("인증실패")
                messages.error(request, "로그인에 실패했습니다. 다시 시도하세요.")    
        except User.DoesNotExist:
            print("인증실패: 사용자 없음")
    return render(request, "users/login.html")



def logout_view(request):
    logout(request)
    messages.success(request, "성공적으로 로그아웃을 했습니다!!")
    return render(request, "users/logout.html")

def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)
#        print(form)
        if form.is_valid():
            user_data = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'gender': form.cleaned_data['gender'],
                'birth': form.cleaned_data['birth'],
                'profile_image': form.cleaned_data['profile_image'],
                'short_description': form.cleaned_data['short_description'],
            }
            form.save()  # 유저 생성 후 저장
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")             
            try:
                user=User.objects.get(username=username)
                if user.check_password(password):
                    print("인증성공")
                    login(request, user)
    #               print(login(request, user))
                    return render(request, "users/userinfo.html")
                else:
                    print("인증실패")
                    messages.error(request, "로그인에 실패했습니다. 다시 시도하세요.")    
            except User.DoesNotExist:
                print("인증실패: 사용자 없음") 
            
    else:
        form = SignupForm()
        #print(form)   
    context = {"form": form}
    return render(request, "users/signup.html", context)



def usersinfo_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, "users/userinfo.html")