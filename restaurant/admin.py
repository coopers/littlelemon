from django.contrib import admin
from .models import Booking, Menu

my_models = [Booking, Menu]
admin.site.register(my_models)
