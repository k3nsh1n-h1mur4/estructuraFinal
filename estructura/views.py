import os
import sqlite3
from PIL import Image

from .connection import Connection

from django.core.paginator import Paginator

from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, BaseUserCreationForm

from .forms import UserRegistrationForm, EstructuraRegistrationForm
from .models import EstructuraModel

def index(request):
    return HttpResponse('Hola Index')

def createUser(request):
    title = 'Registro de Usuario'
    error = None
    form = UserRegistrationForm
    return render(request, 'registration/createUser.html', {'form': form, 'title': title})

    
def login(request):
    title = 'Login'
    error = None
    form = AuthenticationForm
    request.session['id'] = request.POST['username']
    print(request.session,get('username'))
    return render(request, 'registration/login.html', {'form': form, 'title': title})   

@login_required
def logout(request):
    if request.method == 'POST':
        logout.flush()
    
    

def upload_handle_img(img, name):
    with Image.open(img) as img:
        print(img)
        img.save(os.path.join(settings.UPLOAD_FILES, name))
        
        
def getLastId():
    cnx = Connection.getConnection()
    cur = cnx.cursor()
    cur.execute("SELECT id FROM estructuratbl order by id desc limit 1;")
    rowid = cur.fetchone()
    cnx.commit()
    print(rowid)
    if not rowid[0]:
        return
    else: return rowid[0] + 1
    

@login_required    
def new_register(request):
    title = 'Nuevo Registro'
    error = None
    form = EstructuraRegistrationForm()
    if request.method == 'POST':
        form = EstructuraRegistrationForm(request.POST, request.FILES)
        matricula = request.POST['matricula']
        nombre = request.POST['nombre']
        fotot = request.FILES['fotot']
        fotof = request.FILES['fotof']
        fechan = request.POST['fechan']
        categoria= request.POST['categoria']
        centtrabact= request.POST['centtrabact']
        adscant= request.POST['adscant']
        turno= request.POST['turno']
        domicilio= request.POST['domicilio']
        colonia= request.POST['colonia']
        municipio= request.POST['municipio']
        seccional= request.POST['seccional']
        numcel= request.POST['numcel']
        correo= request.POST['correo']
        resp100= request.POST['resp100']
        resp10= request.POST['resp10']
        parttrab= request.POST['parttrab']
        infadic= request.POST['infadic']
        descansos= request.POST['descansos']
        vacprog= request.POST['vacprog']
        servicio= request.POST['servicio']
        promocion= request.POST['promocion']
        movilizacion= request.POST['movilizacion']
        respasig= request.POST['respasig']
        engrupo= request.POST['engrupo']
        asisreunion= request.POST['asisreunion']
        status= request.POST['status']
        upload_handle_img(fotot, fotot.name)
        folder = os.path.join(settings.BASE_DIR, 'images')
        imgPersonPath = os.path.join(folder, fotot.name)
        
        upload_handle_img(fotof, fotof.name)
        imgSignPath = os.path.join(folder, fotof.name)
        data = [
            (getLastId(),matricula,nombre,imgPersonPath,imgSignPath,fechan,categoria,centtrabact,adscant,turno,domicilio,colonia,municipio,seccional,numcel,correo,resp100,resp10,parttrab,infadic,
             descansos,vacprog,servicio,promocion,movilizacion,respasig,engrupo,asisreunion,status,request.user.id),
        ]
        cnx = Connection.getConnection()
        cur = cnx.cursor()
        
        cur.executemany("INSERT INTO estructuratbl VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", data)
        cnx.commit()
        cur.close()
        
        
    return render(request, 'new_register.html', {'form': form, 'title': title})    
    
@login_required    
def list(request):
    title = 'Listado General'
    error = None
    if request.method == 'GET':
        cnx = Connection.getConnection()
        cur = cnx.cursor()
        cur.execute("SELECT * FROM estructuratbl WHERE user_id = {0}".format(request.user.id) )
        ctx = cur.fetchall()
        cnx.commit()
        total = len(ctx)
        paginator = Paginator(ctx, 15)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        cur.close()
        print(total)
        print(request.user.username)
    return render(request, 'list.html', {'title': title, 'error': error, 'page_obj' : page_obj, 'total': total})

@login_required
def details(request, id):
    id = id
    title = 'Detalles del Registro'
    error = None
    cnx = Connection.getConnection()
    cur = cnx.cursor()
    cur.execute('SELECT * FROM estructuratbl WHERE id = {0};'.format(id))
    ctx = cur.fetchone()
    if not ctx:
        error = 'No hay Registros por Mostrar'
    cnx.commit()
    cur.close()
    return render(request, 'details.html', {'title': title, 'error': error, 'ctx': ctx})


@login_required
def delete(request,id):
    id = id
    cnx = Connection.getConnection()
    cur = cnx.cursor()
    cur.execute("DELETE FROM estructuratbl WHERE id = {0}".format(id))
    cnx.commit()
    cur.close()
    return redirect('list')
    