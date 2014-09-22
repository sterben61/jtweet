from django.conf.urls import patterns, url


urlpatterns = patterns('jtweet.jtweetapp.views',
    url(r'^$', 'index', name='index'),

    url(r'^followers/$', 'followers', name='followers'),
)
