from django.contrib import admin
from sample.models import *

# Register your models here.


class ApplianceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roomid')


class WirelessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'wireless', 'name')

admin.site.register(Appliances, ApplianceAdmin)
admin.site.register(Wireless, WirelessAdmin)
admin.site.register(RoomID, RoomAdmin)