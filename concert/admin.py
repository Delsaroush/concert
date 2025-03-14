from django.contrib import admin

from concert.models import Concert, Ticket

# Register your models here.
admin.site.register(Concert)
admin.site.register(Ticket)
