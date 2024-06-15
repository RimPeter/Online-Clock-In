from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Create User Form

class CreateUserForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
# - Login User Form

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    
    
# - Create Record Form

class CreateRecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']

# - Update Record Form

class UpdateRecordForm(forms.ModelForm):
        
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']       