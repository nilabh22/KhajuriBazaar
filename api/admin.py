from django.contrib import admin

# Register your models here.

from .models import Borrower, Stateloan

admin.site.register(Borrower)
admin.site.register(Stateloan)