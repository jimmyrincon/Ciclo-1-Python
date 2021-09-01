#Aplicación CRUD - Lista de Tareas Pendientes
#############################################
#Inicialización de tareas (desde el código)
tareas = {
    '01': { 
            'descripcion':'Ir a mercar',
            'estado' : 'pendiente',
            'tiempo' : 60            
           },
    '02': { 
            'descripcion':'Estudiar',
            'estado' : 'pendiente',
            'tiempo' : 180            
           }, 
    '03': { 
            'descripcion':'Hacer ejercicio',
            'estado' : 'pendiente',
            'tiempo' : 50            
           } 
}

def mostrarMenu():
    print('-- Aplicacion CRUD para Tareas --')
    print('1. Adicionar Tareas')
    print('2. Consultar Tareas')
    print('3. Actualizar Tareas')
    print('4. Eliminar Tareas')
    print('5. Salir')

def createDiccionatioTarea():
    print('Por favor ingrese los datos para CREAR la nueva tarea')
    codigoTarea = input('Por favor ingrese el CODIGO de la nueva tarea: ')
    descripcion = input('Por favor ingrese la DESCIRPCION de la nueva tarea: ')
    estado = input('Por favor ingrese el ESTADO de la nueva tarea: ')
    tiempo = int(           input(  'Por favor ingrese el TIEMPO de la nueva tarea: '    )        )
    dicTarea = {
        codigoTarea : {
            'descripcion' : descripcion,
            'estado' : estado,
            'tiempo' : tiempo
        }
    }
    return dicTarea

def createTarea():
    dicTareaNueva = createDiccionatioTarea()
    codigoTarea = list(dicTareaNueva.keys())
    codigoTareas = list(tareas.keys())
    if codigoTarea in codigoTareas :
        print('El codigo de la tarea ya existe, intentelo de nuevo.')
    else:
        tareas.update(dicTareaNueva)
        print('La tarea fue creada satisfactoriamente.')

def consultar():
    print('-------------------------------------------------------')
    for (codigoTarea, tarea) in tareas.items():
        print(f'La tarea con codigo {codigoTarea} consiste en:')
        print(f'Descripcion: {tarea["descripcion"]}')
        print(f'Estado: {tarea["estado"]}')
        print(f'Tiempo: {tarea["tiempo"]}')
        print('-------------------------------------------------------')

def actualizar():
    codigoTarea = input('Por favor introduzca el codigo de la tarea que desea actualizar: ')
    llaves = list(  tareas.keys()  )
    if codigoTarea in llaves :
        #proceso para actualizar
        descripcionIntroducida = input('Por favor ingrese la DESCRIPCION de la tarea actualizada: ')
        estadoIntroducida = input('Por favor ingrese el ESTADO de la tarea actualizada: ')
        tiempoIntroducida = int(           input(  'Por favor ingrese el TIEMPO de la tarea actualizada: '    )        )
        tarea = {
            codigoTarea : {
                'descripcion': descripcionIntroducida,
                'estado' : estadoIntroducida,
                'tiempo' : tiempoIntroducida   
            }
        }
        tareas.update(tarea)
    else:
        print('El codigo introducido no existe, intentelo de nuevo.')
        opcion = input('Si desea crear una tarea ingrese 1.')
        if opcion == '1' :
            createTarea()

def eliminar():
    print('-------------------------------------------------------')
    codigoTarea = input('Por favor introduzca el codigo de la tarea que desea eliminar: ')
    try:
        #tareas.pop(codigoTarea)
        del tareas[codigoTarea]
        print('La tarea fue eliminada correctamente.')
    except:
        print('Error, eliminando la tarea')

#####################################################
#Aqui inicia el codigo, lo de arriba son definiciones.
opcion = 0
while opcion != '5' :
    mostrarMenu()
    opcion = input('Ingrese una opcion: ')
    if opcion == '1':
        createTarea()
    elif opcion == '2':
        consultar()
    elif opcion == '3' :
        actualizar()
    elif opcion == '4':
        eliminar()
print('El programa ha finalizado correctamente.')