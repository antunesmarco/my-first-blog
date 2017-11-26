from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.real_state_search, name='real_state_search'),
	url(r'^imoveis/(?P<pk>\d+)/$', views.country_detail, name='country_detail'),
]

