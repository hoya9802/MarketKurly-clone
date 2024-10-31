from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
 #   path("usersinfo", views.usersinfo_view, name="usersinfo"),
    path('userinfo/', views.usersinfo_view, name='userinfo'),
    
]