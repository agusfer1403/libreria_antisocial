from django import forms


class GuitarraForm(forms.Form):
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    color = forms.CharField(max_length=50)
    numero_cuerdas = forms.IntegerField(min_value=1)

class BajoForm(forms.Form):
    marca = forms.CharField(max_length=100) 
    modelo = forms.CharField(max_length=100)
    color = forms.CharField(max_length=50)
    

class BateriaForm(forms.Form):
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    color = forms.CharField(max_length=50)
    numero_piezas = forms.IntegerField(min_value=1)

class GuitarraElectricaForm(forms.Form):
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    color = forms.CharField(max_length=50)
    numero_cuerdas = forms.IntegerField(min_value=1)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)


