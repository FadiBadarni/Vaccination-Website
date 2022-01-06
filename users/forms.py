from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()   # email field addition

    class Meta:      # nested namespace for configs
        model = User   # model to be affected
        fields = ['username', 'email', 'password1', 'password2']   # fields in order


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class ManageHolidayForm(forms.Form):
    holiday = forms.ChoiceField(choices=WEEK_DAYS, required=False)