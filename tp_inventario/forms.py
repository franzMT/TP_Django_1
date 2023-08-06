from django import forms
from . import models

class ProductoFrom(forms.ModelForm):
    class Meta:
        model = models.TablaProductos
        fields = ['nombre','precio','stock','categoria','origen']