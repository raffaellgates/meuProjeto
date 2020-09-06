from django.shortcuts import render
from django.http import HttpResponse
from enquetes.models import Enquete

def bemvindo(request):
    return render(request, 'bemvindo.html')

def enquete(request,enquete_id):
	enquete = Enquete.objects.get(id=enquete_id)

	return render(request,'enquete.html',{"enquete":enquete})