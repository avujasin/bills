from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #registration, edit
from django import forms #registration
from django.contrib.auth.models import User #registration
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','password1','password2']

class BillForm(ModelForm):
    class Meta:
        model = MonthlyBills
        fields =  ['description','price', 'payment_date','category']
        widgets = {
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'payment_date':forms.DateInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }