from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import requests
import blockcypher
#from blockcypher import get_blockchain_overview
from .forms import GetDataForm, cryptoForm, blockForm
from django.views.generic import TemplateView
from django.urls import reverse


#good working example of requesting form input, in this case a ethereum block number
#then passing that in a post back to the page and using the block number to query the 
#blockcypher api for information about the block.
class Blocks(TemplateView):
    Template_name = 'api_web/Blocks.html'

    def get(self, request):
        form = blockForm()
        args =  { 'Title' : 'Block Get Request', 'form' : form}  
        return render(request, self.Template_name, args )

    def post(self, request):
        form = blockForm(request.POST)
        if form.is_valid():
            element = form.cleaned_data['Block']
            response = requests.get('https://api.blockcypher.com/v1/eth/main/blocks/%s' %(element))
            Block = response.json()
            args =  {'Title' : 'Block Post Request', 'form' : form, 'Block' : Block}   
        return render(request, self.Template_name, args )


class Ethereum(TemplateView):
    Template_name = 'api_web/Ethereum.html'

    def get(self, request):
        main = requests.get('https://api.blockcypher.com/v1/eth/main')
        lastblock = main.json()['height']
        detail = requests.get(main.json()['latest_url'])
        message = detail.json()
        args =  {'lastblock' : lastblock, 'Title' : 'Ethereum Lastblock Get Request', 'message' : message}  
        return render(request, self.Template_name, args )

    def post(self, request):
        args =  {'Title' : 'Post Request'}   
        return render(request, self.Template_name, args )


#below is a good working example of taking an input, in this case a coin - BTC works -
#then passing form collected data via post and rendering a html file
#after running a number of api / rest calls to get more information
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


class Ethereumback(TemplateView):
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



