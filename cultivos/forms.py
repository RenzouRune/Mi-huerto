from django import forms 
from .models import Cultivo

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = ['nombre', 'tipo', 'descripcion', 'siembra', 'cosecha']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows':3}),
        }
    