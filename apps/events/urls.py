from django.conf.urls import url
from events import views

app_name = 'events'

urlpatterns = [
    url(r'(?P<slug>[0-9A-Za-z\-]+)$', views.event_detail, name='event-detail'),
    url(r'$', views.home, name='home'),
]