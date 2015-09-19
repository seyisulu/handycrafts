from django.contrib import admin
from registration.models import Artisan, Skill, Producer, Product, User, State, LocalGovernment

# Register your models here.

admin.site.register(Artisan)
admin.site.register(Skill)
admin.site.register(Producer)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(State)
admin.site.register(LocalGovernment)
