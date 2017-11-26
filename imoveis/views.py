from django.shortcuts import render
from .models import Country

def real_state_search(request):
#	for c in Country.objects.all():
		#countries += c.country + ' ' + c.currency_symbol
	countries = Country.objects.all()

	return render(request, 'imoveis/real_state_search.html', {'countries':countries})


