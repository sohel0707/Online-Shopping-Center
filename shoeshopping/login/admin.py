from django.contrib import admin
from .models import SingleShoes,Shoes,Orders,OrderUpdate
# Register your models here.
admin.site.register(Shoes)
admin.site.register(SingleShoes)
admin.site.register(Orders)
admin.site.register(OrderUpdate)