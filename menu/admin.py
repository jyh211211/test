from django.contrib import admin
from .models import Dish , Drink , Pasta, Risotto
# Register your models here.

admin.site.register(Dish)
admin.site.register(Drink)
admin.site.register(Risotto)
admin.site.register(Pasta)