from django.shortcuts import render
from django.http import HttpResponse
from .models import Enquete

def bemvindo(request):
    return render(request, 'bemvindo.html')

def enquete(request,enquete_id):
	enquete = Enquete()

	if enquete_id == 1:
		enquete = Enquete('Quantos planetas Terra cabem dentro do Sol?', '27/08/2020')
	elif enquete_id == 2:
		enquete = Enquete('Em que lugar vivem mais cangurus do que pessoas?', '28/08/2020')
	elif enquete_id == 3:
		enquete = Enquete('Qual a ciência que estuda a atmosfera da Terra e a climatologia', "29/08/2020")

	return render(request,'enquete.html',{"enquete":enquete})