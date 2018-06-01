from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import requests
from .forms import GetDataForm
from django.views.generic import TemplateView


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



