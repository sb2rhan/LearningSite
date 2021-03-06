from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Firstname'
        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Lastname'
        self.fields['groups'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'groups', 'password1', 'password2']
