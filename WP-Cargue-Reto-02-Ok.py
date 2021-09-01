def reporte_ferreteria(productos_vendidos:dict):
    pre_1 = productos_vendidos['producto1']['precio']
    pre_2 = productos_vendidos['producto2']['precio']
    pre_3 = productos_vendidos['producto3']['precio']
    total_precio = pre_1 + pre_2 + pre_3 
    iva_1 = productos_vendidos['producto1']['iva'] * productos_vendidos['producto1']['precio']
    iva_2 = productos_vendidos['producto2']['iva'] * productos_vendidos['producto2']['precio']
    iva_3 = productos_vendidos['producto3']['iva'] * productos_vendidos['producto3']['precio']
    total_impuestos = iva_1 + iva_2 + iva_3
    nombreproducto1 = productos_vendidos ['producto1'] ['nombre']
    nombreproducto2 = productos_vendidos ['producto2'] ['nombre']
    nombreproducto3 = productos_vendidos ['producto3'] ['nombre']
    mensaje = (f'Los productos reportados son: {nombreproducto1} , {nombreproducto2} , {nombreproducto3}')
    reporte_ferreteria2 = { 
        'precio_total':total_precio,
        'impuestos_total':total_impuestos, 
        'reporte':mensaje
    }
    return(reporte_ferreteria2)

print(reporte_ferreteria({'producto1' : {'nombre' : 'Varilla','precio' : 35250,'iva'    : 0.05,},'producto2' : {'nombre' : 'Cemento','precio'  : 60500,'iva'    : 0.15,},'producto3' : {'nombre' : 'Tubo PVC','precio'  : 10300,'iva'    : 0.,}}))
print(reporte_ferreteria({'producto1' : {'nombre' : 'Llave','precio' : 1500,'iva'    : 0,},'producto2' : {'nombre' : 'Cemento','precio'  : 60500,'iva'    : 0.15,},'producto3' : {'nombre' : 'Tornillos','precio'  : 22500,'iva'    : 0.19,}}))