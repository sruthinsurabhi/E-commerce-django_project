from django import forms
from .models import UserRegister




class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = '__all__'

        labels = {'u_name': ' Name',
                  'u_phone': 'Phone Number',
                  'u_email': 'E-mail',
                  'u_pass':'Password',
                  'u_pass1':'Confirm Password'
                  }






