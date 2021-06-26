from django.shortcuts import render
from perfis.models import Perfil

def index(request):   #para trazer todos os perfis (uma lista se houver)
    return render(request, 'index.html', { 'perfis' : Perfil.objects.all()})

def exibir(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)
	# precisa agora buscar do banco
    return render(request, 'perfil.html', { "perfil" : perfil})
