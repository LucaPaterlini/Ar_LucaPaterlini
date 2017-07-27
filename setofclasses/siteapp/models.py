# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_init
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_rating(value):
    if not(type(value) is int and 0<value<11):
        raise ValidationError(
            _('%(value) is not in the right rating range 1-10'),
            params={'value': value},
        )

# Site Class
class Site(models.Model):
    Url = models.URLField()
    Date = models.DateField()
    Rating = models.IntegerField(validators=[validate_rating])

    @classmethod
    def create(cls,*args):
         return cls(Url=args[0], Date=args[1], Rating=args[2])


    def save(self, *args, **kwargs):
        self.full_clean()
        super(Site, self).save(*args, **kwargs)

