from django.urls import reverse
from tempfile import template
from urllib import request
from .forms import FormConnexion
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from cv.models import Stage,Formation,Competance,Type
from django.contrib.auth import authenticate, login, logout



def index (request):
      template =loader.get_template('index.html')
      
      return HttpResponse (template.render())

def info (request):
      template =loader.get_template('info.html')
      context={
            'nom':'Mohamed Aziz',
            'prenom':'Belhadj hassine',
            'adresse':'115 Rue de la plage-8080 Menzel Temime',
            'telephone':'56168717'}
      return HttpResponse (template.render(context,request))

def stage (request):
    stage = Stage.objects.all().values()
    template = loader.get_template('stage.html')
    context = { 'stage' : stage,}
    return HttpResponse (template.render(context,request))

def formation (request):
    formation = Formation.objects.all().values()
    type= Type.objects.all().values()
    template = loader.get_template('formation.html')
    context = { 'formation' : formation,
    'type':type}
    return HttpResponse (template.render(context,request))

def competance (request):
    competance = Competance.objects.all().values()
    template = loader.get_template('competance.html')
    context = { 'competance' : competance,}
    return HttpResponse (template.render(context,request))

def type(request):
      type= Type.objects.all().values()
      template =loader.get_template('type.html')
      context = {'type':type,}
      return HttpResponse (template.render(context,request))

def update_typ(request, id):
    
    type = Type.objects.get(id=id)
    template = loader.get_template('updateType.html')
    context = {
    'type':type,
    }
    return HttpResponse(template.render(context, request))    

def update_typ_action(request, id):
    n = request.POST['nomType']
    d = request.POST['description']
    typ = Type.objects.get(id=id)
    typ.nomType = n
    typ.description= d
    typ.save()
    return HttpResponseRedirect(reverse('type'))

def add_type(request):
    template = loader.get_template('addtype.html')
    type = Type.objects.all().values()
    context = {'type' :type,}
    return HttpResponse(template.render(context,request))

def add_type_action(request):
    n = request.POST['nomType']
    d = request.POST['description']
    type = Type(nomType=n,description=d)
    type.save()
    return HttpResponseRedirect(reverse('type'))

def delete_type(request, id):
    ty = Type.objects.get(id=id)
    ty.delete()
    return HttpResponseRedirect(reverse('type'))

def add_formation(request):
    formation = Formation.objects.all().values()
    type = Type.objects.all().values()
    template = loader.get_template('addformation.html')
    context = {
    'formation': formation,
    'type':type,}
    return HttpResponse(template.render(context, request))

def add_formation_action(request):
    int = request.POST['intitule']
    lieux = request.POST['lieux']
    da = request.POST['date']
    nomty = request.POST['s']
    noms = Type.objects.get(id=nomty)
    formation = Formation(intitule=int,lieu=lieux,date=da,type=noms)
    formation.save()
    return HttpResponseRedirect(reverse('formation'))

def del_formation(request, id):
    formation = Formation.objects.get(id=id)
    formation.delete()
    return HttpResponseRedirect(reverse('formation'))

def update_formation(request, id):
    formation = Formation.objects.get(id=id)
    type = Type.objects.all().values()
    template = loader.get_template('upadateformation.html')
    context = {
    'formation': formation,
    'type':type, }
    return HttpResponse(template.render(context, request))


def update_formation_action(request, id):
    a = request.POST['intitule']
    b = request.POST['lieu']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    c = request.POST['s']
    rech = Type.objects.get(id=c)
    formation = Formation.objects.get(id=id)
    formation.intitule=a
    formation.lieu=b
    formation.type=rech
    formation.save()
    return HttpResponseRedirect(reverse('formation'))

def connect (request):
    connect_form = FormConnexion()
    return render(request, 'connexion.html', {'connect_form' :connect_form})

def signIn(request):
    connect_form = FormConnexion()
    username = request.POST['login']
    password = request.POST['mot2pass']
    user = authenticate(request, username=username,password=password)
    if user is not None:
        login(request, user)
        request.session['username'] = username
        return HttpResponseRedirect(reverse('formation'))
    else:
        return render(request, 'connexion.html', {'connect_form' :connect_form,'error':True})

def signOut(request):
   logout(request)
   return HttpResponseRedirect(reverse('connect'))
