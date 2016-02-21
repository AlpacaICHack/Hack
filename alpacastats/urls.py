from django.conf.urls import url

from views import apis, public_views

urlpatterns = [
    url(r'^$', public_views.home, name='index'),
    url(r'^pool/(?P<event_id>[0-9]+)$', public_views.pool, name='pool'),
    url(r'^statistics/(?P<event_id>[0-9]+)$', public_views.statistics, name='statistics'),
    url(r'^api/events$', apis.events, name='events_api'),
    url(r'^api/pool$', apis.pool, name='pool_api'),
    url(r'^api/vote_track$', apis.vote_track, name='vote_track_api'),
    url(r'^api/movement$', apis.movement, name='movement_api'),
    url(r'^api/vote$', apis.vote, name='vote_api'),
    url(r'^api/add_request$', apis.add_request, name='requests_api'),
    url(r'^api/current_track$', apis.current_track, name='current_track'),
]