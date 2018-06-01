from django import forms

class GetDataForm(forms.Form):
    employeeID = forms.CharField()
