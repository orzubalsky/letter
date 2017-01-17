from django.conf.urls import url
from letters import views

app_name = 'letters'

urlpatterns = [
    url(r'(?P<slug>[0-9A-Za-z\-]+)$', views.letter_detail, name='letter-detail'),
    url(r'$', views.home, name='home'),
]
