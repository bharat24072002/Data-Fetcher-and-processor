import requests
import pandas as pd
from django.shortcuts import render
from .models import Data

def fetch_and_store_data(request):
    # Fetch data from API
    response = requests.get('https://api.example.com/data')
    data = response.json()

    # Process data using Pandas
    df = pd.DataFrame(data)
    df['value'] = df['value'] * 1.1  # Example transformation

    # Store data in database
    for _, row in df.iterrows():
        Data.objects.create(name=row['name'], value=row['value'])

    return render(request, 'data.html', {'data': df.to_html()})


# Create your views here.
