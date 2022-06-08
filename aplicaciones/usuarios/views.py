from django.shortcuts import render, redirect
from .models import Usuarios, TipoDocumentos, TipoSangre
from .forms import UsuarioForm

# Create your views here.

def usuario_urls(request):
    usuarios = Usuarios.objects.raw('SELECT u.id, u.nombre, u.apellido, u.telefono, u.correo, u.edad, td.tipo_documento, u.numero_de_documento, tp.tipo_de_persona,ts.tipo_rh FROM usuarios as u, tipo_documentos as td, categoria_de_personas as tp, tipo_sangre as ts where u.tipo_de_documento = td.id AND u.tipo_de_persona = tp.id AND u.rh = ts.id;')
    user = {'usuarios': usuarios}
    return render(request ,'usuarios/usuarios.html',user)

# def usuario_urls(request):
#     usuarios = Usuarios.objects.all()
#     tipo_documento = Usuarios.objects.raw('SELECT u.id, u.nombre, u.apellido, u.telefono, u.correo, u.edad, td.tipo_documento, u.numero_de_documento, tp.tipo_de_persona,ts.tipo_rh FROM usuarios as u, tipo_documentos as td, categoria_de_personas as tp, tipo_sangre as ts where u.tipo_de_documento = td.id AND u.tipo_de_persona = tp.id AND u.rh = ts.id;')
#     user = {'usuarios': usuarios}
#     tipo_d = {'tipo_documento':tipo_documento}
#     return render(request ,'usuarios/usuarios.html', (user, tipo_d))

def insertar_usuarios(request):
    td = TipoDocumentos.objects.all()
    ts = TipoSangre.objects.all()
    if(request.method == 'GET'):
        forms = UsuarioForm()
        tipos = { 'td': td,'ts': ts , 'form': forms}
    else:
        forms = UsuarioForm(request.POST)   
        tipos = { 'td': td,'ts': ts ,'form': forms }
        if forms.is_valid():
            forms.save()
            return redirect('usuario_urls')
    return render(request, 'usuarios/add_users.html',tipos )

def editar_usuarios(request,id):
    td = TipoDocumentos.objects.all()
    ts = TipoSangre.objects.all()
    usuario = Usuarios.objects.get(id = id)
    if(request.method == 'GET'):
        forms = UsuarioForm(instance= usuario)
        tipos = { 'td': td,'ts': ts , 'form': forms}
    else:
        forms = UsuarioForm(request.POST, instance= usuario)   
        tipos = { 'td': td,'ts': ts ,'form': forms }
        if forms.is_valid():
            forms.save()
            return redirect('usuario_urls')
    return render(request, 'usuarios/Update_users.html',tipos )

def borrar_usuarios(request,id):
    usuario = Usuarios.objects.get(id = id)
    usuario.delete()
    return redirect('usuario_urls')