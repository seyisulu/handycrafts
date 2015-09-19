from django.conf.urls import include, url, patterns
from registration import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^artisan/(?P<pk>\d+)/$', views.ArtisanView.as_view(), name='artisanDetail'),
    url(r'^producer/(?P<pk>\d+)/$', views.ProducerView.as_view(), name='producerDetail'),
    url(r'^user/(?P<pk>\d+)/$', views.UserView.as_view(), name='userDetail'),
    url(r'^artisan/register$', views.ArtisanCreate.as_view(), name='artisan_add'),
    url(r'^artisan/profile/settings/(?P<pk>\d+)/$', views.ArtisanUpdate.as_view(), name='artisan_update'),
    url(r'^producer/register$', views.ProducerCreate.as_view(), name='producer_add'),
    url(r'^producer/profile/settings/(?P<pk>\d+)/$', views.ProducerUpdate.as_view(), name='producer_update'),
    url(r'^user/register$', views.UserCreate.as_view(), name='user_add'),
    url(r'^user/profile/settings/(?P<pk>\d+)/$', views.UserUpdate.as_view(), name='user_update'),
]
