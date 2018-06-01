from django import forms


class GetDataForm(forms.Form):
    employeeID = forms.CharField()

class cryptoForm(forms.Form):
    element = forms.CharField(label='Currency Symbol')
    blockcount = forms.CharField(label='Block Count', required=False)
    
class blockForm(forms.Form):
    Block = forms.CharField(label='Block Number:')
    nonce = forms.CharField(label='Nonce:', required=False)

