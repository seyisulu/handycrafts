from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Artisan(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=30)
    state = models.CharField(max_length=10)
    lga = models.CharField(max_length=20)
    skill = models.ForeignKey(Skill)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/register/artisan/details/%i' % self.id
#        return reverse('register.views.ArtisanView.as_view()', kwargs={'pk': self.pk})


class Product(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=30)
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=20)
    product = models.ManyToManyField(Product)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/register/producer/details/%i' % self.id
#       return reverse('register.views.ArtisanView.as_view()', kwargs={'pk': self.pk})


class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=30)
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/register/user/details/%i' % self.id
#       return reverse('register.views.ArtisanView.as_view()', kwargs={'pk': self.pk})
