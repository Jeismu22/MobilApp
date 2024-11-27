from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarpetaForm, ProyectoForm, TareaForm
from .models import Carpeta, Proyecto, Tarea


def bienvenida(request):
    return render(request, 'bienvenida.html')


def dashboard(request):
    if request.method == 'POST':
        # Crear carpeta
        if 'crear_carpeta' in request.POST:
            form = CarpetaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')

        # Crear proyecto
        elif 'crear_proyecto' in request.POST:
            form = ProyectoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')

        # Crear tarea
        elif 'crear_tarea' in request.POST:
            form = TareaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')

    # Obtener todas las carpetas, proyectos y tareas para mostrar
    carpetas = Carpeta.objects.all()
    proyectos = Proyecto.objects.all().order_by('fecha_limite')  # Ordenar proyectos por fecha más cercana
    tareas = Tarea.objects.all().order_by('fecha_limite')  # Ordenar tareas por fecha más cercana

    # Renderizar la página con los formularios y datos
    return render(request, 'dashboard.html', {
        'carpeta_form': CarpetaForm(),
        'proyecto_form': ProyectoForm(),
        'tarea_form': TareaForm(),
        'carpetas': carpetas,
        'proyectos': proyectos,
        'tareas': tareas
    })


# Vista para eliminar un elemento
def eliminar_item(request, modelo, item_id):
    if modelo == 'carpeta':
        item = get_object_or_404(Carpeta, id=item_id)
    elif modelo == 'proyecto':
        item = get_object_or_404(Proyecto, id=item_id)
    elif modelo == 'tarea':
        item = get_object_or_404(Tarea, id=item_id)
    item.delete()
    return redirect('dashboard')


# Vista para editar un elemento
def editar_item(request, modelo, item_id):
    if modelo == 'carpeta':
        item = get_object_or_404(Carpeta, id=item_id)
        form_class = CarpetaForm
    elif modelo == 'proyecto':
        item = get_object_or_404(Proyecto, id=item_id)
        form_class = ProyectoForm
    elif modelo == 'tarea':
        item = get_object_or_404(Tarea, id=item_id)
        form_class = TareaForm

    if request.method == 'POST':
        form = form_class(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # Obtener los valores de los checkboxes
            completado = 'completado' in request.POST
            proceso = 'proceso' in request.POST
            pendiente = 'pendiente' in request.POST
            retrasado = 'retrasado' in request.POST

            # Actualizar los estados en el modelo de tarea (si aplica)
            if modelo == 'tarea':
                item.completado = completado
                item.proceso = proceso
                item.pendiente = pendiente
                item.retrasado = retrasado
                item.save()
            #return redirect('dashboard')
            return redirect('graficas', modelo=modelo)

    else:
        form = form_class(instance=item)

    return render(request, 'editar_item.html', {'form': form, 'modelo': modelo})

def editar_item(request, modelo, item_id):
    if modelo == 'carpeta':
        item = get_object_or_404(Carpeta, id=item_id)
        form_class = CarpetaForm
    elif modelo == 'proyecto':
        item = get_object_or_404(Proyecto, id=item_id)
        form_class = ProyectoForm
    elif modelo == 'tarea':
        item = get_object_or_404(Tarea, id=item_id)
        form_class = TareaForm

    if request.method == 'POST':
        form = form_class(request.POST, instance=item)
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect('dashboard')  # Redirigir al dashboard después de guardar

    else:
        form = form_class(instance=item)

    return render(request, 'editar_item.html', {'form': form, 'modelo': modelo})


def graficas(request):
    # Contar los estados para tareas
    completado_tareas = Tarea.objects.filter(estado='completado').count()
    proceso_tareas = Tarea.objects.filter(estado='en_proceso').count()
    pendiente_tareas = Tarea.objects.filter(estado='pendiente').count()
    retrasado_tareas = Tarea.objects.filter(estado='retrasado').count()

    # Contar los estados para proyectos
    completado_proyectos = Proyecto.objects.filter(estado='completado').count()
    proceso_proyectos = Proyecto.objects.filter(estado='en_proceso').count()
    pendiente_proyectos = Proyecto.objects.filter(estado='pendiente').count()
    retrasado_proyectos = Proyecto.objects.filter(estado='retrasado').count()

    # Contar los estados para carpetas
    completado_carpetas = Carpeta.objects.filter(estado='completado').count()
    proceso_carpetas = Carpeta.objects.filter(estado='en_proceso').count()
    pendiente_carpetas = Carpeta.objects.filter(estado='pendiente').count()
    retrasado_carpetas = Carpeta.objects.filter(estado='retrasado').count()

    # Sumar los resultados de tareas, proyectos y carpetas
    completado_total = completado_tareas + completado_proyectos + completado_carpetas
    proceso_total = proceso_tareas + proceso_proyectos + proceso_carpetas
    pendiente_total = pendiente_tareas + pendiente_proyectos + pendiente_carpetas
    retrasado_total = retrasado_tareas + retrasado_proyectos + retrasado_carpetas

    return render(request, 'graficas.html', {
        'completado_total': completado_total,
        'proceso_total': proceso_total,
        'pendiente_total': pendiente_total,
        'retrasado_total': retrasado_total,
    })
