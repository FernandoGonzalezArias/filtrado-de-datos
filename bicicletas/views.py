from django.shortcuts import render
from .models import Salesorderheader
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    codigo_orden = request.GET.get('codigo_orden')
    ciudad = request.GET.get('ciudad')
    codigo_postal = request.GET.get('codigo_postal')
    fecha_entrega_desde = request.GET.get('fecha_entrega_desde')

    ordenes = Salesorderheader.objects.all()

    if codigo_orden:
        ordenes = ordenes.filter(salesorderid__startswith=codigo_orden)
    if ciudad:
        ordenes = ordenes.filter(shiptoaddressid__city__istartswith=ciudad)
    if codigo_postal:
        ordenes = ordenes.filter(shiptoaddressid__postalcode__icontains=codigo_postal)
    if fecha_entrega_desde:
        ordenes = ordenes.filter(shipdate__gte=fecha_entrega_desde)
        
    if fecha_entrega_desde:
        try:
            fecha_entrega_desde = datetime.datetime.strptime(fecha_entrega_desde, "%d-%m-%y").date()
            ordenes = ordenes.filter(shipdate__gte=fecha_entrega_desde)
        except ValueError:
            pass 

    # la variable p 500 es para que muestre los primeros 500 datos 
    # para dar mas velocidad a la carga de datos y a los filtrados
    # ya que la base de datos es demasiado grande y deja lenta la ejecucion.
    p50 = ordenes[:50] 
    context = {'ordenes': p50}
    return render(request, 'index.html', context)





