# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Residuo(models.Model):
    name = models.CharField('Nome', max_length = 100)
    codigo = models.CharField('Código', max_length = 7)
    created_at = models.DateTimeField('Criado em', auto_now_add = True)
    updated_at = models.DateTimeField('Criado em', auto_now = True)

    def __str__(self):
        return self.name 
