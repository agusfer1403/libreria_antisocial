from django.shortcuts import render
from .forms import GuitarraForm, BajoForm, BateriaForm, SearchForm
from .models import Guitarra, Bajo, Bateria

def guitarra_form_view(request):
    if request.method == 'POST':
        form = GuitarraForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GuitarraForm()
    return render(request, 'guitarra_form.html', {'form': form})

def bajo_form_view(request):
    if request.method == 'POST':
        form = BajoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BajoForm()
    return render(request, 'bajo_form.html', {'form': form})

def bateria_form_view(request):
    if request.method == 'POST':
        form = BateriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BateriaForm()
    return render(request, 'bateria_form.html', {'form': form})

def search_view(request):
    results = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
           
            results += Guitarra.objects.filter(marca__icontains=query)
            results += Bajo.objects.filter(marca__icontains=query)
            results += Bateria.objects.filter(marca__icontains=query)
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form, 'results': results})
