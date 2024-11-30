from django import forms
from .models import ChaiVerity

class ChaiVerityForm(forms.Form):
    chai_verity = forms.ModelChoiceField(queryset=ChaiVerity.objects.all(), label="Select Chai Veriety")
    

