from django.shortcuts import render, redirect, get_object_or_404
from .forms import GuitarraForm, BajoForm, BateriaForm, GuitarraElectricaForm, SearchForm
from .models import Guitarra, Bajo, Bateria, GuitarraElectrica



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

def guitarra_electrica_form_view(request):
    if request.method == 'POST':
        form = GuitarraElectricaForm(request.POST)
        if form.is_valid():
            guitarraelectrica = GuitarraElectrica(
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                color=form.cleaned_data['color'],
                numero_cuerdas=form.cleaned_data['numero_cuerdas']
            )
            guitarraelectrica.save()
            return redirect('crear-guitarraelectrica')
    else:
        form = GuitarraElectricaForm()
    return render(request, 'crear-guitarraelectrica.html', {'form': form})

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


def listar_guitarras(request):
    guitarras = Guitarra.objects.all()
    return render(request, 'listar_guitarras.html', {'guitarras': guitarras})

def agregar_guitarra(request):
    if request.method == 'POST':
        form = GuitarraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_guitarras')
    else:
        form = GuitarraForm()
    return render(request, 'instrumentos/agregar_guitarra.html', {'form': form})

def editar_guitarra(request, pk):
    guitarra = get_object_or_404(Guitarra, pk=pk)
    if request.method == 'POST':
        form = GuitarraForm(request.POST, instance=guitarra)
        if form.is_valid():
            form.save()
         
            return redirect('detalle_guitarra', pk=guitarra.pk)
    else:
        form = GuitarraForm(instance=guitarra)
    return render(request, 'editar_guitarra.html', {'form': form, 'guitarra': guitarra})


def eliminar_guitarra(request, pk):
    guitarra = get_object_or_404(Guitarra, pk=pk)
    guitarra.delete()
    return redirect('listar_guitarras')


def listar_bajos(request):
    bajos = Bajo.objects.all()
    return render(request, 'listar_bajos.html', {'bajos': bajos})

def agregar_bajo(request):
    if request.method == 'POST':
        form = BajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_bajo')
    else:
        form = BajoForm()
    return render(request, 'agregar_bajo.html', {'form': form})


def editar_bajo(request, pk):
    bajo = get_object_or_404(Bajo, pk=pk)
    if request.method == 'POST':
        form = BajoForm(request.POST, instance=bajo)
        if form.is_valid():
            form.save()
            return redirect('listar_bajos')
    else:
        form = BajoForm(instance=bajo)
    return render(request, 'editar_bajo.html', {'form': form, 'bajo': bajo})

def eliminar_bajo(request, pk):
    bajo = get_object_or_404(Bajo, pk=pk)
    bajo.delete()
    return redirect('listar_bajo')

def listar_baterias(request):
    baterias = Bateria.objects.all()
    return render(request, 'listar_baterias.html', {'baterias': baterias})

def agregar_bateria(request):
    if request.method == 'POST':
        form = BateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_baterias')
    else:
        form = BateriaForm()
    return render(request, 'agregar_bateria.html', {'form': form})

def editar_bateria(request, pk):
    bateria = get_object_or_404(Bateria, pk=pk)
    if request.method == 'POST':
        form = BateriaForm(request.POST, instance=bateria)
        if form.is_valid():
            form.save()
            return redirect('listar_baterias')
    else:
        form = BateriaForm(instance=bateria)
    return render(request, 'instrumentos/editar_bateria.html', {'form': form, 'bateria': bateria})

def eliminar_bateria(request, pk):
    bateria = get_object_or_404(Bateria, pk=pk)
    bateria.delete()
    return redirect('listar_baterias')


def listar_guitarras_electricas(request):
    guitarras_electricas = GuitarraElectrica.objects.all()
    return render(request, 'instrumentos/listar_guitarras_electricas.html', {'guitarras_electricas': guitarras_electricas})


def agregar_guitarra_electrica(request):
    if request.method == 'POST':
        form = GuitarraElectricaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_guitarras_electricas')
    else:
        form = GuitarraElectricaForm()
    return render(request, 'instrumentos/agregar_guitarra_electrica.html', {'form': form})

def editar_guitarra_electrica(request, pk):
    guitarra_electrica = get_object_or_404(GuitarraElectrica, pk=pk)
    if request.method == 'POST':
        form = GuitarraElectricaForm(request.POST, instance=guitarra_electrica)
        if form.is_valid():
            form.save()
            return redirect('listar_guitarras_electricas')
    else:
        form = GuitarraElectricaForm(instance=guitarra_electrica)
    return render(request, 'instrumentos/editar_guitarra_electrica.html', {'form': form, 'guitarra_electrica': guitarra_electrica})

def eliminar_guitarra_electrica(request, pk):
    guitarra_electrica = get_object_or_404(GuitarraElectrica, pk=pk)
    guitarra_electrica.delete()
    return redirect('listar_guitarras_electricas')

def detalle_guitarra(request, pk):
    guitarra = get_object_or_404(Guitarra, pk=pk)
    return render(request, 'detalle_guitarra.html', {'guitarra': guitarra})


def detalle_bajo(request, pk):
    bajo = get_object_or_404(Bajo, pk=pk)
    return render(request, 'detalle_bajo.html', {'bajo': bajo})

def detalle_bateria(request, pk):
    bateria = get_object_or_404(Bateria, pk=pk)
    return render(request, 'detalle_bateria.html', {'bateria': bateria})

def detalle_guitarra_electrica(request, pk):    
    GuitarraElectrica = get_object_or_404(GuitarraElectrica, pk=pk)
    return render(request, 'detalle_guitarra_electrica.html', {'guitarraelectrica': GuitarraElectrica})
