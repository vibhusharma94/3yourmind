from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Company(models.Model):
    """The Company model."""

    name = models.CharField(_('company name'), max_length=255)
    created = models.DateTimeField(_('date created'), auto_now_add=True)

    def __unicode__(self):
        return self.name


class Material(models.Model):
    """The Material model."""

    name = models.CharField(_('material name'), max_length=255)
    created = models.DateTimeField(_('date created'), auto_now_add=True)

    def __unicode__(self):
        return self.name


class Manufacturer(models.Model):
    """The Manufacturer model."""

    company = models.ForeignKey(Company, related_name='materials')
    material = models.ForeignKey(Material, related_name='manufacturers')
    unit_price = models.DecimalField(_('Manufacturing price per unit volume'), max_digits=6, decimal_places=2)
    created = models.DateTimeField(_('date created'), auto_now_add=True)

    def __unicode__(self):
        return self.company.name
