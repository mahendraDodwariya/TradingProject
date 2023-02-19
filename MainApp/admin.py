from django.contrib import admin

from .models import(
    File,
    Candle,
)
# Registering our models in database

@admin.register(File)
class File(admin.ModelAdmin):
    list_display = ['id' , 'file']
 
@admin.register(Candle)
class Candle(admin.ModelAdmin):
    list_display = ['id' ,'open', 'high','low','close']

# Register your models here.
