from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterFormIntern(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)
    birth_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2')
        help_texts = {
            'username': None,
            'first_name': None,
            'last_name': None,
            'email': None,
            'birth_date': None,
            'password1': None,
            'password2': None,
        }

class RegisterFormCompany(UserCreationForm):
    company_name = forms.CharField(max_length=30, required=True)
    tax_id = forms.IntegerField()
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    foundation_year = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = User
        fields = ('username', 'company_name', 'tax_id', 'email', 'foundation_year', 'password1', 'password2')
        help_texts = {
            'username': None,
            'company_name': None,
            'tax_id': None,
            'email': None,
            'foundation_year': None,
            'password1': None,
            'password2': None,
        }
