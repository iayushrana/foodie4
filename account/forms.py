from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)#to take passwords
    cpassword=forms.CharField(widget=forms.PasswordInput,label="confirm_password")#to take passwords
    phone_no=forms.CharField(widget=forms.TextInput,label="Enter phone number :")
    full_name=forms.CharField(widget=forms.TextInput,label="Full name :")

#attrs={'class':'form-control form-control-sm','placeholder':'+91 1234567890'},

    class Meta:
        model=User
        fields=['username','full_name','email','password','cpassword','phone_no']
