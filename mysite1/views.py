from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def form_view(request):
	if request.method.upper() == 'POST':
		name = request.POST['your_name']

	if name != "keith":
		return HttpResponse("bad name")
	else:
		return HttpResponse("that's good name")
	elif request.method.upper() == "GET":
		return render(request, 'form_view.html')