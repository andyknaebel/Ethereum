from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import requests
from .forms import GetDataForm, cryptoForm
from django.views.generic import TemplateView

class Ethereum(TemplateView):
    Template_name = 'api_web/Ethereum.html'

    def get(self, request):
        main = requests.get('https://api.blockcypher.com/v1/eth/main')
        message = main.json()['height']
        detail = requests.get(main.json()['latest_url'])
        lastblock = detail.json()
        args =  {'lastblock' : lastblock, 'Title' : 'Get Request', 'message' : message}  
        return render(request, self.Template_name, args )

    def post(self, request):
        args =  {'Title' : 'Post Request'}   
        return render(request, self.Template_name, args )

class crypto(TemplateView):
    Template_name = 'api_web/crypto.html'

    def get(self, request):
        form = cryptoForm()
        args = {'form' : form}
        return render(request, self.Template_name, args )

    def post(self, request):
        form =cryptoForm(request.POST)
        if form.is_valid():
            element = form.cleaned_data['element'].upper()
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/%s.json' %(element))
            #response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json')
            price = response.json()['bpi'][element]['rate']
            getblockcount = requests.get('https://blockchain.info/q/getblockcount')
            lastblock = getblockcount.json()
            probability = requests.get('https://blockchain.info/q/probability')
            probability = probability.json()
            args =  {'probability' : probability, 'lastblock' : lastblock, 'form' : form, 'element' : element , 'price' : price }   
        return render(request, self.Template_name, args )





def api_webview(request):
    response = requests.get('http://localhost:8000/api/employee/')
    employees = response.json()
    context = {'employees' : employees}
    return render(request, 'api_web/index.html', context) 

class api_getone(TemplateView):
    Template_name = 'api_web/getone.html'

    def get(self, request):
        form = GetDataForm()
        return render(request, self.Template_name, {'form' : form} )

    def post(self, request):
        form = GetDataForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['employeeID']

        args =  {'form' : form, 'text' : text }   
        return render(request, self.Template_name, args )



