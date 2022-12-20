from django import forms
from .models import records
class RecordForm(forms.ModelForm):
    class Meta:
        model = records
        fields = "__all__"
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Doctor': forms.TextInput(attrs={'class': 'form-control'}),
        }