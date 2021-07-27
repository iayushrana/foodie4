from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)#to take passwords
    cpassword=forms.CharField(widget=forms.PasswordInput,label="confirm_password")#to take passwords
    phone_no=forms.CharField(widget=forms.TextInput,label="enter_phone_number :")

#attrs={'class':'form-control form-control-sm','placeholder':'+91 1234567890'},

    class Meta:
        model=User
        fields=['username','email','password','cpassword','phone_no']




PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 50)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

