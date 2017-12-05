# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class HeroClass(models.Model):                                                               
    name = models.CharField(max_length=100)
    def __unicode__(self):                                                                   
        return unicode(self.name)
                                                                                             
class Game(models.Model):                                                                    
    name = models.CharField(max_length=100)
    def __unicode__(self):                                                                   
        return unicode(self.name)

class Heroes(models.Model):
    name = models.CharField(max_length=100, default='')
    game = models.ForeignKey(Game, default=1) 
    picture = models.CharField(max_length=300, default='')
    hero_class = models.ForeignKey(HeroClass, default=1)
    def __unicode__(self):                                                                   
        return unicode(self.name)