from django.shortcuts import render
import requests
import datetime
# Create your views here.
def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Kolkata'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b452b74fd5752f39aad48dfce90e2b08'
    PARAMS = {'units':'metric'}
    return render(request,'index.html') # Render the home.html template