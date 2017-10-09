from mainApp.models import userInfo,userRatings
from django import forms
from django.contrib.auth.models import User

class userInfoForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(
        attrs = {
        'type':"text",
        'class':"inputFields",
        'id':"username",
        'name':"username",
        'placeholder':"Username",
        'value':"" ,
        'oninput':"return userNameValidation(this.value)",
        'required':"True",
        }
    ))
    email = forms.EmailField(widget = forms.EmailInput(
            attrs = {
            'type':"text",
            'class':"inputFields",
            'id':"email",
            'name':"email",
            'placeholder':"Email",
            'value':"" ,
            'oninput':"return emailValidation(this.value)",
            'required':"True",
            }
        ))
    password = forms.CharField(widget = forms.TextInput(
        attrs = {
        'type':"password",
        'class':"inputFields",
        'id':"password",
        'name':"password",
        'placeholder':"Password",
        'value':"" ,
        'oninput':"return passwordValidation(this.value)",
        'required':"True",
        }
    ))
    # portfolio = forms.URLField(required = False)
    # pic = forms.ImageField(required= False)

    class Meta:
        model = User
        fields = ('username','email','password')
        help_texts = {
            'username': None,
            'email': None,
        }

# class userRatingsForm(forms.ModelForm):
#
