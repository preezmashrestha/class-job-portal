from django.contrib import admin
from .models import Admin,Orders,Customer,Items,Problems,OrderItem
# Register your models here.


admin.site.register(Admin)
admin.site.register(Orders)
admin.site.register(Customer)
admin.site.register(Items)
admin.site.register(Problems)
admin.site.register(OrderItem)