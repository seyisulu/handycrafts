from django.shortcuts import render, HttpResponse, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from registration.models import Artisan, State, LocalGovernment, User

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView
from registration.forms import SearchForm, ArtisanForm, UserForm

from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from twilio.rest import TwilioRestClient


class ArtisanCreate(CreateView):
    model = Artisan
    form_class = ArtisanForm
    exclude = ['created_on', 'updated_on']
    template_name = 'registration/forms/artisan_register.html'

    def post(self, request, *args, **kwargs):
        print("submitted form")
        form = ArtisanForm(request.POST)
        return super(ArtisanCreate, self).form_valid(form)


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    exclude = ['created_on', 'updated_on']
    template_name = 'registration/forms/user_register.html'

    def post(self, request, *args, **kwargs):
        print("submitted form")
        form = UserForm(request.POST)
        return super(UserCreate, self).form_valid(form)


class ArtisanUpdate(UpdateView):
    model = Artisan
    form_class = ArtisanForm
    exclude = ['created_on', 'updated_on']
    template_name = 'registration/forms/artisan_form.html'

    def post(self, request, *args, **kwargs):
        print("submitted form")
        form = ArtisanForm(request.POST)
        return super(ArtisanUpdate, self).form_valid(form)


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    exclude = ['created_on', 'updated_on']
    template_name = 'registration/forms/user_form.html'

    def post(self, request, *args, **kwargs):
        print("submitted form")
        form = UserForm(request.POST)
        return super(UserUpdate, self).form_valid(form)


class ArtisanView(DetailView):
    model = Artisan
    template_name = 'registration/details/artisan_detail.html'
    context_object_name = 'artisanDetail'


class UserView(DetailView):
    model = User
    template_name = 'registration/details/user_detail.html'
    context_object_name = 'userDetail'

class ArtisanList(ListView):
    """
        lists all the artisans in the database
    """
    model = Artisan
    queryset = Artisan.objects.all()
    template_name = 'registration/details/artisan_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArtisanList, self).get_context_data(**kwargs)
        context['artisan_list'] = Artisan.objects.order_by('-rating')
        return context


def do_reg(msg, frm):
    """
    :param msg: message from the user
    :param frm: the sender's phone number
    :return: message to be sent to the sender

    msg must be of the form: name skill state local-government
    """
    print("Did Reg")

    lg = LocalGovernment.objects.filter(name__contains=msg[3])[0]
    st = State.objects.filter(name__contains=msg[2])[0]
    x = Artisan(name=msg[0], phone=frm, skill=msg[1], lga=lg, state=st)
    x.save()

    return "You are registered %s" % msg[0]


def do_search(msg):
    """
    :param msg: message from the user
    :return: result of the search query in the database

    msg must be of the form: skill state
    """
    print("Did Search")
    x = Artisan.objects.filter(state__name__contains=msg[1]).filter(skill__contains=msg[0])[:5]
    result = ""

    if x.exists():
        for i in range(len(x)):
            result = x[i].name + ', ' + x[i].phone + ';\n'
        return str("You searched for a %s" % msg[0] + ".Here are your results:\n" + result)
    else:
        return "Sorry there are no " + msg[0] + "s in " + msg[1] + ". Perhaps you could help register them."


def do_change(msg):
    """
    :param msg: message from the user
    :return: message confirming that change was successful or not

    msg must be of the form: old_number new_number
    """
    print("Did Change")
    x = Artisan.objects.get(phone=msg[0])
    if x.DoesNotExist:
        return 'Sorry that number has not been registered.' \
               + '\n to register send: reg name skill state local-government'
    else:
        x.phone = msg[1]
        x.save(force_update=True)
        return "Congratulations your new number is %s" % msg[1]


def do_rate(msg):
    """
    :param msg: message from the user
    :return:  message confirming that rating was successful
    msg must be of the form: artisan_phone_number rating
    """
    print("Did Rate")
    x = Artisan.objects.filter(phone=msg[0])[0]
    x.rating = int(msg[1]) / x.number_of_ratings
    x.save(force_update=True)
    print(x.rating)
    return "Thanks for rating %s stars, we appreciate your feedback" % msg[1]


@twilio_view
def sms(request):
    """
    :param request: message received from twillo
    :return: message to be sent to twillo
    """
    msg = request.POST.get('Body', '')
    sender = request.POST.get('From', '')

    scheme = msg.split(' ')[0].upper()

    # split message and route to appropriate function
    if scheme == 'REG':
        msg = do_reg(msg.split(' ')[1:], sender)
    elif scheme == 'SEARCH':
        msg = do_search(msg.split(' ')[1:])
    elif scheme == 'CHANGE':
        msg = do_change(msg.split(' ')[1:])
    elif scheme == 'RATE':
        msg = do_rate(msg.split(' ')[1:])

    r = Response()
    r.message(msg)

    return r


def ring(request):
    # Find these values at https://twilio.com/user/account
    account_sid = "ACd591840ff2d7aa1130f11a038a7dd91d"  # replace with your account_sid
    auth_token = "81e5d567cb610bc9b50160ec46ba5dbd"  # replace with your auth_token
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to="+2348161759814", from_="+14847341528",  # replace with your phone_num
                                     body="It works!")
    return HttpResponse(str(message))


def index(request):
    context = {'search_form': SearchForm}
    return render_to_response('registration/home.html',context)


def search(request):
    if request.method == 'GET':
        # If the form has been submitted...
        # SearchForm was defined in the previous section
        form = SearchForm(request.GET)  # A form bound to the GET data
        if form.is_valid():  # All validation rules pass
            skill = form.cleaned_data['find']
            print("Found the ", skill)
            context = {'artisan_list': Artisan.objects.filter(skill__contains=skill)}
            return render_to_response('registration/details/artisan_list.html', context)
    else:
        form = SearchForm()  # An unbound form
    return HttpResponseRedirect(reverse('account:index'))