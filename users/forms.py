from django import forms
from django.core.exceptions import ValidationError

from users.models import User

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()
    first_name =  forms.CharField()
    last_name = forms.CharField()
    gender = forms.CharField()
    birth = forms.CharField()
    profile_image = forms.ImageField()
    short_description = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명({username})은 이미 사용중입니다")
        return username
    
    def save(self, commit=True):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        gender= self.cleaned_data["gender"]
        birth= self.cleaned_data["birth"]
        profile_image = self.cleaned_data["profile_image"]
        short_description = self.cleaned_data["short_description"]
        
        user = User.objects.create_user(
                    username=username,
                    email = email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    gender=gender,
                    birth=birth,
                    profile_image=profile_image,
                    short_description=short_description,
        )
        print(user.username, user.email)
        if commit:                       
               user.save()
        return user