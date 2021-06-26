from django.contrib import admin
from api.models import Customer

class Customers(admin.ModelAdmin):
    list_display = ('req_status','id', 'first_name', 'last_name', 'email', 'gender', 'company', 'city', 'title', 'lat', 'lgn')
    list_display_links = ('id', 'first_name')
    search_fields = ('id', 'first_name',)
    list_per_page_ = 30

admin.site.register(Customer, Customers)