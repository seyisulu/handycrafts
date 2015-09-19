from django.forms import ModelForm
from registration.models import Artisan, Producer, User


class ArtisanForm(ModelForm):
    class Meta:
        model = Artisan
        exclude = ['created_on', 'updated_on']
        fields = ['name', 'phone', 'name', 'phone', 'address', 'emailAddress', 'state', 'lga', 'skill']


class ProducerForm(ModelForm):
    class Meta:
        model = Producer
        exclude = ['created_on', 'updated_on']
        fields = ['name', 'phone', 'name', 'phone', 'address', 'emailAddress', 'state', 'lga', 'product']


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['created_on', 'updated_on']
        fields = ['name', 'phone', 'name', 'phone', 'address', 'emailAddress', 'state', 'lga']

