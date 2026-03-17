from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from mi_aplicacion.models import Escuela, Maestro
from mi_aplicacion.form import EscuelaForm, MaestroForm

class Home(View):
    def get(self, request):
        cdx = {
            "titulo":"Home",
            "subtitulo":"Bienvenido a mi primer aplicacion"
            }
        return render(request, "home/home.html", cdx)
    
class Escuelas(View):
    def get(self, request):
        escuelas = Escuela.objects.all()
        cdx = {
            "titulo":"Escuelas",
            "subtitulo":"Lista de escuelas",
            "escuelas":escuelas
            }
        return render(request, "escuelas/escuelas.html", cdx)
    
class EscuelaAlta(View):
    def get(self, request):
        form = EscuelaForm()
        cdx={
            "titulo":"Escuela",
            "subtitulo":"Alta de Escuela",
            "form":form,
            "action_type":"create"
        }
        return render(request, "escuelas/CRUD.html", cdx)

    def post(self, request):
        form = EscuelaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        return redirect("home")

class EscuelaEditar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
            "titulo":"Escuela",
            "subtitulo":"Editar Escuela",
            "form":form,
            "action_type":"edit"
        }
        return render (request, "escuelas/CRUD.html", cdx)

    def post(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST, request.FILES, instance = escuela)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        return redirect("home")
    
class EscuelaEliminar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
            "titulo":"Escuela",
            "subtitulo":"Eliminar Escuela",
            "form":form,
            "action_type":"delete"
        }
        return render (request, "escuelas/CRUD.html", cdx)

    def post(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST, request.FILES, instance = escuela)
        if form.is_valid():
            escuela.delete()
            return redirect('escuelas')
        return redirect("home")
    

class Maestros(View):
    def get(self, request):
        maestros = Maestro.objects.all()
        cdx = {
            "titulo":"Maestros",
            "subtitulo":"Lista de maestros",
            "maestros":maestros
            }
        return render(request, "maestros/maestros.html", cdx)

    
class MaestroAlta(View):
    def get(self, request):
        form = MaestroForm(action_type='create')
        cdx={
            "titulo":"Maestros",
            "subtitulo":"Alta de Maestro",
            "form":form,
            "action_type":"create"
        }
        return render(request, "maestros/CRUD.html", cdx)
    def post(self, request):
        form = MaestroForm(request.POST, request.FILES, action_type='create')
        if form.is_valid():
            form.save()
            return redirect('maestros')
        return redirect("home")
    
class MaestroEditar(View):
    def get(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestro, action_type='edit')
        cdx={
            "titulo":"Maestro",
            "subtitulo":"Editar Maestro",
            "form":form,
            "action_type":"edit"
        }
        return render (request, "maestros/CRUD.html", cdx)

    def post(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro, action_type='edit')
        if form.is_valid():
            form.save()
            return redirect('maestros')
        return redirect("home")

class MaestroEliminar(View):
    def get(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestro, action_type='delete')
        cdx={
            "titulo":"Maestro",
            "subtitulo":"Eliminar Maestro",
            "form":form,
            "action_type":"delete"
        }
        return render (request, "maestros/CRUD.html", cdx)

    def post(self, request, id):
        maestros = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestros, action_type='delete')
        if form.is_valid():
            maestros.delete()
            return redirect('maestros')
        return redirect("home")
    
