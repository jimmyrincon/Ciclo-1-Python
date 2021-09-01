def reporte_ferreteria(productos_vendidos:dict):
    total_precio = productos_vendidos["producto1"]["precio"] + productos_vendidos["producto2"]["precio"] + productos_vendidos["producto3"]["precio"]
    total_impuestos = (productos_vendidos["producto1"]["iva"] * productos_vendidos["producto1"]["precio"] + productos_vendidos["producto2"]["iva"] * productos_vendidos["producto2"]["precio"] + productos_vendidos["producto3"]["iva"] * productos_vendidos["producto3"]["precio"])
    nombreproducto1 = productos_vendidos ["producto1"] ["nombre"]
    nombreproducto2 = productos_vendidos ["producto2"] ["nombre"]
    nombreproducto3 = productos_vendidos ["producto3"] ["nombre"]
    mensaje = (f"Los productos reportados son: {nombreproducto1}, {nombreproducto2}, {nombreproducto3}")
    reporte = { 
        "precio_total" : {total_precio},
        "impuestos_total" : {total_impuestos}, 
        "reporte" : {mensaje}
    }
    return(reporte)
print(reporte_ferreteria({'producto1' : {'nombre' : 'Varilla','precio' : 35250,'iva'    : 0.05,},'producto2' : {'nombre' : 'Cemento','precio'  : 60500,'iva'    : 0.15,},'producto3' : {'nombre' : 'Tubo PVC','precio'  : 10300,'iva'    : 0,}}))