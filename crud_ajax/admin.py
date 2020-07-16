from django.contrib import admin

# Register your models here.
from .models import CrudUser,Product,Tasks,Books

admin.site.register(CrudUser)
admin.site.register(Product)
admin.site.register(Tasks)
admin.site.register(Books)
