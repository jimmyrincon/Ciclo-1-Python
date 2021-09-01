def reporte_ferreteria(productos_vendidos):
    dict(productos_vendidos)
    (productos_vendidos) = {
    'producto1':{
        'nombre':"nombreproducto1",
        'precio':precio1,
        'iva':porcentaje_iva1,
    },
    'producto2':{
        'nombre':"nombreproducto2",
        'precio':precio2,
        'iva':porcentaje_iva2,
    },
    'producto3':{
        'nombre':"nombreproducto3",
        'precio':precio3,
        'iva':porcentaje_iva3,
    }
}



nombreproducto1= "Varilla"
nombreproducto2= "Cemento"
nombreproducto3= "Tubo PVC"
precio1= 35250
precio2= 60500
precio3= 10300
porcentaje_iva1= 0.05
porcentaje_iva2= 0.15
porcentaje_iva3= 0
iva1=((precio1*porcentaje_iva1)/100)*100
iva2=((precio2*porcentaje_iva2)/100)*100
iva3=((precio3*porcentaje_iva3)/100)*100

precio_total=(precio1+precio2+precio3)
impuestos_total=(iva1+iva2+iva3)
reporte=(nombreproducto1+" "+nombreproducto2+" "+nombreproducto3)
reporte2=("precio total",(precio1+precio2+precio3),"impuestos total",(iva1+iva2+iva3,"Los productos reportados son:",(nombreproducto1+" "+nombreproducto2+" "+nombreproducto3)))

print(precio_total)
print(impuestos_total)
print(reporte)
print(reporte2)

nombreproducto1= "llave"
nombreproducto2= "Cemento"
nombreproducto3= "Tornillos"
precio1= 1500
precio2= 60500
precio3= 22500
porcentaje_iva1= 0
porcentaje_iva2= 0.15
porcentaje_iva3= 0.19
iva1=((precio1*porcentaje_iva1)/100)*100
iva2=((precio2*porcentaje_iva2)/100)*100
iva3=((precio3*porcentaje_iva3)/100)*100

precio_total=(precio1+precio2+precio3)
impuestos_total=(iva1+iva2+iva3)
reporte=(nombreproducto1+" "+nombreproducto2+" "+nombreproducto3)
reporte2=("precio total",(precio1+precio2+precio3),"impuestos total",(iva1+iva2+iva3,"Los productos reportados son:",(nombreproducto1+" "+nombreproducto2+" "+nombreproducto3)))

print(precio_total)
print(impuestos_total)
print(reporte)
print(reporte2)