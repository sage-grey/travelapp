from django.contrib import admin
from .models import product
from .models import team


# Register your models here.
admin.site.register(product)
admin.site.register(team)