from django import forms
from .models import FinancialRecord

class RecordForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(
            format='%d-%m-%Y',
            attrs={'placeholder': 'DD-MM-YYYY'}
        )
    )

    class Meta:
        model = FinancialRecord
        fields = ['amount', 'type', 'category', 'date', 'notes']