from django.contrib import admin

# Register your models here.
from inventory.models import Product, Family, Location, Transaction

admin.site.register(Product)
admin.site.register(Family)
admin.site.register(Location)
admin.site.register(Transaction)