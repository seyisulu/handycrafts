from django.conf.urls import url, patterns
from registration import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artisan/(?P<pk>\d+)/$', views.ArtisanView.as_view(), name='artisanDetail'),
    url(r'^user/(?P<pk>\d+)/$', views.UserView.as_view(), name='userDetail'),
    url(r'^artisan/register$', views.ArtisanCreate.as_view(), name='artisan_register'),
    url(r'^user/register$', views.UserCreate.as_view(), name='user_register'),
    url(r'^artisan/profile/settings/(?P<pk>\d+)/$', views.ArtisanUpdate.as_view(), name='artisan_update'),
    url(r'^user/profile/settings/(?P<pk>\d+)/$', views.UserUpdate.as_view(), name='user_update'),
    url(r'^list_artisans/$', views.ArtisanList.as_view(), name='artisan_list'),
    url(r'^search/$', views.search, name='search'),
    url(r'^sms/$', views.sms),
    url(r'^ring/$', views.ring),
]

# TODO: perfect the registration page for user and artisan
# TODO: adjust the artisan and user update page
# TODO: include Artisan Details page
