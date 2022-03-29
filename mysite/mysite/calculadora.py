from django.shortcuts import render
from django.http import HttpResponse
import math

def index(request):
    return render(request,'index.html')

def add(request):
    opcion = request.GET['opciones']
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    if opcion == 'suma':
       respuesta = float(num1)+ float(num2)
    elif opcion == 'resta':
        respuesta = float(num1)-float(num2)
    elif opcion == 'multiplicacion':
        respuesta = float(num1)*float(num2)
    elif opcion == 'division':
        respuesta = float(num1)/float(num2)
    elif opcion == 'raiz':
        RNum1 = math.sqrt(float(num1))
        RNum2 = math.sqrt(float(num2))
        respuesta = 'num1 ='+str(RNum1) + ', num2 = '+str(RNum2)
    elif opcion == 'exponencial':
        respuesta = math.pow(float(num1),float(num2))
    elif opcion == 'logaritmo':
        respuesta = math.log(float(num1),float(num2))
    else:
        respuesta ="Opción incorrecta"
    
    return render(request,'resultado.html',{ 'result': respuesta} )