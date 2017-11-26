from django.shortcuts import render
from .models import Country
from django.shortcuts import render, get_object_or_404

def real_state_search(request):
	countries = Country.objects.all()
	return render(request, 'imoveis/real_state_search.html', {'countries':countries})

def country_detail(request, pk):
	country = get_object_or_404(Country, pk=pk)
	return render(request, 'imoveis/country_detail.html', {'country':country})


