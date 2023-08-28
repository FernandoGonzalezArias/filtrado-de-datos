from django.contrib import admin
from .models import Salesorderheader

class SalesorderheaderAdmin(admin.ModelAdmin):
    list_display = ('salesorderid', 'shipdate','duedate','status', 'addressline1', 'city')

    def addressline1(self, obj):
        if obj.shiptoaddressid:
            return obj.shiptoaddressid.addressline1
        return ""

    def city(self, obj):
        if obj.shiptoaddressid:
            return obj.shiptoaddressid.city
        return ""

admin.site.register(Salesorderheader, SalesorderheaderAdmin)


