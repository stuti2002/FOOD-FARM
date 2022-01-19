from typing import runtime_checkable
from home.models import Contact,Order
from django.contrib import admin

# Register your models here.
admin.site.register(Contact)
admin.site.register(Order)
