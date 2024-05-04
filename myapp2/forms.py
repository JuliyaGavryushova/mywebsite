from django import forms
from .models import Product


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=50,
#                            widget=forms.TextInput(attrs={'class': 'form-control'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
#     price = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     quantity = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     image = forms.ImageField()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']