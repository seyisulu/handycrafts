from django.shortcuts import render, HttpResponse, render_to_response
from django.http import HttpResponseRedirect

from registration.models import Artisan, Producer, User

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from registration.forms import ProducerForm, ArtisanForm, UserForm


# Create your views here.

# def test(request):
#    return render_to_response('home/home_page.html')


class ProducerCreate(CreateView):
    model = Producer
    form_class = ProducerForm
    exclude = ['created_on', 'updated_on']
    template_name = 'registration/forms/producer_form.html'


class ArtisanCreate(CreateView):
    model = Artisan
    form_class = ArtisanForm
    exclude = ['created_on', 'updated_on']
    template_name = 'registration/forms/artisan_form.html'


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    exclude = ['created_on', 'updated_on']
    template_name = 'registration/forms/user_form.html'


class ProducerUpdate(UpdateView):
    model = Producer
    form_class = ProducerForm
    exclude = ['created_on', 'updated_on']
    template_name = 'registration/forms/producer_form.html'


class ArtisanUpdate(UpdateView):
    model = Artisan
    form_class = ArtisanForm
    exclude = ['created_on', 'updated_on']
    template_name = 'registration/forms/producer_form.html'


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    exclude = ['created_on', 'updated_on']
    template_name = 'registration/forms/producer_form.html'


def create_producer(request):
    if request.method == 'POST':
        form = ProducerForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/register')

        else:
            form = ProducerForm()


class ArtisanView(DetailView):
    model = Artisan
    template_name = 'registration/details/artisan_detail.html'
    context_object_name = 'artisanDetail'


class ProducerView(DetailView):
    model = Producer
    template_name = 'registration/details/producer_detail.html'
    context_object_name = 'producerDetail'


class UserView(DetailView):
    model = User
    template_name = 'registration/details/user_detail.html'
    context_object_name = 'userDetail'
