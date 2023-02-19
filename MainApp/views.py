from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import pandas as pd
import csv
# Create your views here.

# This function will create the data for our csv in database with given entries
 
def create_db(file_path):
    df = pd.read_csv(file_path,delimiter = ',')
    print(df.values)
    list_of_csv = [list(row) for row in df.values]

    for l in list_of_csv:
        Candle.objects.create(
            
            
            open = l[3],
            high = l[4],
            low = l[5],
            close = l[6],
          
             
        )

# This function will be used to upload csv file to database 
def uploadcsv(request):
    if( request.method == "POST"):
        file = request.FILES['file']
        obj = File.objects.create(file = file)
        create_db(obj.file)
    return render(request,'MainApp/index.html')