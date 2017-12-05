# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Heroes.models import *

# Register your models here.

class HeroClassAdmin(admin.ModelAdmin):
	list_display = ('name', )
	
class GameAdmin(admin.ModelAdmin):
	list_display = ('name', )
    
class HeroesAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'hero_class', )
    
admin.site.register(HeroClass, HeroClassAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Heroes, HeroesAdmin)