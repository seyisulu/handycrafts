from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse


class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class LocalGovernment(models.Model):
    state_id = models.IntegerField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Artisan(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=30)
    state = models.ForeignKey(State)
    lga = models.ForeignKey(LocalGovernment)
    rating = models.PositiveSmallIntegerField(default=0)
    number_of_ratings = models.PositiveSmallIntegerField(default=0)
    skill = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' skill=' + self.skill

    def get_absolute_url(self):
        return '/account/artisan/%i' % self.id
        # return reverse('register.views.ArtisanView.as_view()', kwargs={'pk': self.pk})


class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=30)
    state = models.ForeignKey(State)
    lga = models.ForeignKey(LocalGovernment)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/account/user/%i' % self.id
        # return reverse('register.views.ArtisanView.as_view()', kwargs={'pk': self.pk})
