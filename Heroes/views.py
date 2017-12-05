# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
#from django.core.context_processors import csrf
from django.shortcuts import loader, render
from django.http import HttpResponse
from .models import *

# Create your views here.



def home(request):
    
    hero_params = dict()
    
    if str(request.GET.get('game_from')) != "None":
        gameobj = Game.objects.get(name=str(request.GET.get('game_from')))
    else:
        gameobj = ""
    
    if str(request.GET.get('class')) != "None":
        classobj = HeroClass.objects.get(name=str(request.GET.get('class')))
    else:
        classobj = ""
    
    if gameobj != "" and classobj != "":
        heroes = Heroes.objects.filter(game=gameobj.id, hero_class=classobj.id)
    elif gameobj != "" and classobj == "":
        heroes = Heroes.objects.filter(game=gameobj.id)
    elif gameobj == "" and classobj != "":
        heroes = Heroes.objects.filter(hero_class=classobj.id)
    elif gameobj == "" and classobj == "":
        heroes = Heroes.objects.all()
        
    if 'searchstring' in request.GET:
        hero_params['name__contains'] = request.GET.get('searchstring')
        heroes = Heroes.objects.filter(**hero_params)
    
        
    t = loader.get_template('home.html')
    c = dict({'heroes': heroes })
    return HttpResponse(t.render(c))


def hero(request, name):
    hero = Heroes.objects.filter(name=name)
    t = loader.get_template('hero.html')
    c = dict({'heroSelect': hero})
    return HttpResponse(t.render(c))
