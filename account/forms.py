from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from account import models


class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
    #     self.fields['first_name'].label = "First"
    #     self.fields['last_name'].label = "Last Name"
    #     self.fields['password1'].label = "Password"
    #     self.fields['password2'].label = "Confirm Password"
        # self.fields['first_name'].required = True
        # self.fields['last_name'].required = True
        # self.fields['email'].required = True
        # self.fields['password1'].required = True
        # self.fields['password2'].required = True
        for field in self.fields:
            self.fields[field].required = True

        self.fields['password1'].error_messages.update({
            'required': 'Password is required'
        })        
        self.fields['password2'].error_messages.update({
            'required': 'Confirm Password is required'
        })

    class Meta:

        model=User

        fields =[
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
            ]
        
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'username': {
                'required': 'Username is required',
                'max_length': 'Username is too long'
            },
            'email': {
                'required': 'Email is required',
                
            }

        }




class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )


    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
      
        if username and password:
            
            self.user = authenticate(username=username, password=password)

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise forms.ValidationError("User Does Not Exist.")

            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")

            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

            

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user