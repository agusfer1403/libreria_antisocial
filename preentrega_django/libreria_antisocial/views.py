from django.shortcuts import render, redirect
from .forms import GuitarraForm, BajoForm, BateriaForm, SearchForm
from .models import Guitarra, Bajo, Bateria


def guitarra_form_view(request):
    if request.method == 'POST':
        form = GuitarraForm(request.POST)
        if form.is_valid():
            guitarra = Guitarra(
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                color=form.cleaned_data['color'],
                numero_cuerdas=form.cleaned_data['numero_cuerdas']
            )
            guitarra.save()
            return redirect('crear-guitarra')
    else:
        form = GuitarraForm()
    return render(request, 'crear-guitarra.html', {'form': form})


def bajo_form_view(request):
    if request.method == 'POST':
        form = BajoForm(request.POST)
        if form.is_valid():
            bajo = Bajo(
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                color=form.cleaned_data['color']
            )
            bajo.save()
            return redirect('crear-bajo')
    else:
        form = BajoForm()
    return render(request, 'crear-bajo.html', {'form': form})


def bateria_form_view(request):
    if request.method == 'POST':
        form = BateriaForm(request.POST)
        if form.is_valid():
           bateria = Bateria(
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                color=form.cleaned_data['color'],
                numero_piezas=form.cleaned_data['numero_piezas']
            )
           bateria.save()
           return redirect('crear-bateria')
    else:
        form = BateriaForm()
    return render(request, 'crear-bateria.html', {'form': form})


def search_view(request):
    results = []
    if request.method == 'POST':
        form =SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']

            results += Guitarra.objects.filter(marca__icontains=query)
            results += Bajo.objects.filter(marca__icontains=query)
            results += Bateria.objects.filter(marca__icontains=query)
    else:
        form =SearchForm()
    return render(request, 'crear-busqueda.html', {'form': form, 'results': results})
