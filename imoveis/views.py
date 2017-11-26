from django.shortcuts import render
from .models import Country
from django.shortcuts import render, get_object_or_404
from .forms import CountryForm
from django.shortcuts import redirect

def real_state_search(request):
	countries = Country.objects.all()
	return render(request, 'imoveis/real_state_search.html', {'countries':countries})

def country_detail(request, pk):
	country = get_object_or_404(Country, pk=pk)
	return render(request, 'imoveis/country_detail.html', {'country':country})

def country_new(request):
	if request.method == "POST":
		form=CountryForm(request.POST)	
		if form.is_valid():
			country = form.save()
			country.save()
			return redirect('country_detail', pk=country.pk)
	else:
		form=CountryForm()
	return render(request, 'imoveis/country_edit.html', {'form': form})

def country_edit(request, pk):
	country = get_object_or_404(Country, pk=pk)
	if request.method == "POST":
		form=CountryForm(request.POST, instance=country)	
		if form.is_valid():
			country = form.save()
			country.save()
			return redirect('country_detail', pk=country.pk)
	else:
		form=CountryForm(instance=country)
	return render(request, 'imoveis/country_edit.html', {'form': form})

