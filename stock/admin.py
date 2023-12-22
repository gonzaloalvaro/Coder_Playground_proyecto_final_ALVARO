from django.contrib import admin

# Register your models here.


from stock.models import ropa,accesorios,anteojos

admin.site.register(ropa)
admin.site.register(accesorios)
admin.site.register(anteojos)