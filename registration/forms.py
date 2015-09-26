from django.forms import ModelForm
from django import forms
from registration.models import Artisan, User


class ArtisanForm(ModelForm):
    class Meta:
        model = Artisan
        exclude = ['created_on', 'updated_on']
        fields = ['name', 'phone', 'address', 'emailAddress', 'state', 'lga', 'skill']


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['created_on', 'updated_on']
        fields = ['name', 'phone', 'address', 'emailAddress', 'state', 'lga']


class SearchForm(forms.Form):
    find = forms.CharField(max_length=50)
