from django.db import models
from datetime import date

class Enquete(object):
	def __init__(self, texto='', data_publicacao=date.today()):
		self.texto = texto
		self.data_publicacao = data_publicacao