from django.contrib import admin
from registration.models import Artisan, User, State, LocalGovernment

# Register your models here.

admin.site.register(Artisan)
admin.site.register(User)
admin.site.register(State)
admin.site.register(LocalGovernment)
