from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.real_state_search, name='real_state_search'),
	url(r'^imoveis/(?P<pk>\d+)/$', views.country_detail, name='country_detail'),
	url(r'^imoveis/new/$', views.country_new, name='country_new'),
	url(r'^imoveis/(?P<pk>\d+)/edit/$', views.country_edit, name='country_edit'),
]

