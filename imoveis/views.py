from django.shortcuts import render

def real_state_search(request):
	return render(request, 'imoveis/real_state_search.html')


