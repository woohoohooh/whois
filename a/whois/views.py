from django.shortcuts import render
from .forms import WhoisForm
import requests

def whois(request):

    if request.method == 'POST':
        form = WhoisForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data['domain']
            url = 'https://api.apilayer.com/whois/check?domain=' + d
            payload = {}
            headers = {
                "apikey": "Ac0CmWiFS9q5TGguVlZqBFjd14yus5d5"
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            result = response.text
            result = result[12:-3]
            if result == 'available':
                result = 'домен свободен'
            else:
                result = 'домен занят'
            return render(request, 'whois/index.html', {'form': form, 'result': result})
    else:
        form = WhoisForm()

    return render(request, 'whois/index.html', {'form': form})