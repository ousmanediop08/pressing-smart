# Register your models here.
from django.contrib import admin
from .models.models import Subscribe, Contact


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'adress', 'created','phone','date_rv','choice','paiement']
    search_fields = ['name', 'email', 'subject','phone']
    list_filter = ['created', ]
    list_per_page = 20

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    search_fields = ['name', 'email', 'subject']
    list_filter = ['created', ]
    list_per_page = 20


admin.site.register( Subscribe, SubscribeAdmin)
admin.site.register( Contact, ContactAdmin)

