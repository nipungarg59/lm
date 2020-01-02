# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from decimal import Decimal

# Create your models here.

class Customer(models.Model):
    """
    Model to store the users
    """
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Order(models.Model):
    """
    Model to store orders of the user
    """
    user = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    chest = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    seat = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    waist = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    low_waist = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    back_width = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    nape_to_waist = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    scye_depth = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    neck_size = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    sleeve_length = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    inside_leg = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    body_rise = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    wrist = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    shirt_length = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    amount_advance = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.00'))
    total_amount =  models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.00'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
