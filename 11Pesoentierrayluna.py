def peso_en_tierra(peso_en_luna):
    peso_en_tierra='el peso de la persona en la tierra'
    peso=peso_en_luna*1.622/9.81
    return(f'El peso en la luna es {peso}')
print(peso_en_tierra(50))