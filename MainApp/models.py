from django.db import models
 
# Create your models here.

# our table in database to store required information from csv file

class File(models.Model):
    file = models.FileField(upload_to = "files")
class Candle(models.Model):
    open = models.FloatField(default = 0.0)
    high = models.FloatField(default = 0.0)
    low = models.FloatField(default = 0.0)
    close = models.FloatField(default = 0.0)
    
     
  
     
    
