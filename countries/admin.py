from django.contrib import admin
from countries.models import *

# Register your models here.
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)

