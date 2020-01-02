# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField

from user_order.models import Customer, Order


# MySpecialAdmin = lambda model: type('SubClass'+model.__name__, (admin.ModelAdmin,), {
#     'list_display': [x.name for x in model._meta.fields],
#     'list_select_related': [x.name for x in model._meta.fields if isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField,))]
# })


class OrderInLine(admin.TabularInline):
    model = Order
    fields = [field.name for field in Order._meta.fields]
    readonly_fields = ('id', 'created_at', 'updated_at',)
    extra = 1
    ordering = ("created_at", )


class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]
    inlines = [
        OrderInLine,
    ]
    ordering = ("created_at", )
    search_fields = ('name', 'number',)


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
