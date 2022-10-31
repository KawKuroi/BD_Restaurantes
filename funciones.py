import Comandos_baseDatos as CBD
from cmath import inf

# ----------------------------------- FUNCION PARA DELIMITAR LA VARIABLE A NUMERO ENTERO Y PONER UN RANGO A ESE NUMERO -----------------
def intLimitado(value,limite=inf,inicio=0):
    while True:
        try:
            value=int(value)
            if value < inicio or value > limite:
                raise Exception
            else:
                return value
        except ValueError:
            value = input('Ingrese un número\n')
        except Exception:
            value = input(f'El número esta fuera de rango\nIngrese un número entre el {inicio} al {limite}\n')

# -------------------------------------------------- MOSTRANDO INFORMACION GENERAL DE RESTAURANTES --------------------------------
def info_restaurantes():
    print('----------- INFO RESTAURANTES --------------')
    restaurantes = CBD.pullDatos('SELECT * FROM Restaurantes')
    for i in restaurantes:
        print(f'{i[1]:15} Tipo de comida = {i[2]:15} Dirección = {i[3]:22} Rango de precios = {i[4]:3} a {i[5]:3}')

# -------------------------------------------------- MOSTRANDO INFORMACION GENERAL DE CALIFICACIONES --------------------------------
def calificaciones_restaurantes():
    print('----------- CALIFICACIONES --------------')
    to=[]
    restaurantes = CBD.pullDatos('SELECT nombre FROM Restaurantes')
    for nombre in restaurantes:
        nota,comentarios = [],[]
        calificaciones = CBD.pullDatos(f'SELECT * FROM Calificaciones WHERE Nombre = "{nombre[0]}"')
        
        for x in calificaciones:
            nota.append(round((x[1]+x[2]+x[3])/3,2))
            comentarios.append(x[4])
        
        prom=round((sum(nota)/len(nota)),2)
        info={'nombre':x[0],'nota':prom,'comentarios':comentarios}
        to.append(info)            

    for i in to:
        print(i['nombre'] + ' --> ' + str(i['nota']) + '⭐ \nComentarios :')
        for x in i['comentarios']:
            print(f'\t{x}')
        print('\n')

# ------------------------------------- FILTROS PARA LA BASE DE DATOS, RESTAURANTES Y CALIFICACIONES --------------------------------
def filtros():
    opcion = intLimitado(input(f'--------------------------------------------\n'
    + '1. Filtrar por tipo de comida\n'
    + '2. Filtrar por rango de precio\n'
    + '3. Filtrar por tiempos de espera promedio\n'
    + '4. Filtrar por calificación promedio de calidad\n'
    + '5. Filtrar por calificación promedio de atención\n'
    + '6. Salir\n'
    + 'Ingrese la opcion que desee:\n'),6,1)
    if opcion == 1:
        Tipo=CBD.pullDatos('SELECT Tipo FROM Restaurantes GROUP BY Tipo')
        posiciones={}
        x=1
        print('Seleccione el un tipo de comida para filtrar restaurantes')
        for i in Tipo:
            print(f'\t{x}) {i[0]}')
            posiciones[x]=i[0]
            x+=1

        seleccionar=intLimitado(input(f'\nIngrese la opción deseada:\n'),x)
        for pos,tipo in posiciones.items():
            if seleccionar == pos:
                filtrados=CBD.pullDatos(f'SELECT Nombre FROM Restaurantes WHERE Tipo = "{tipo}"')
                print(f'------ RESTAURANTES CON TIPO DE COMIDA {tipo} ------\n')                
                for i in filtrados:
                    print('-->',i[0])

    if opcion == 2:
        orden=intLimitado(input('¿Como desea organizar el rango de precios?\n'
        +'1. Ascendiente (Más caro a económico)\n'
        +'2. Descendiente (Más económico a caro)\n'
        +'3. Regresar\n'),3,1)
        print('------------- RANGO DE PRECIOS -------------\n')
        if orden == 1:
            ordenados=CBD.pullDatos(f'SELECT Nombre,Valor_minimo,Valor_maximo FROM Restaurantes ORDER BY Valor_minimo asc, Valor_maximo asc')
            for i in ordenados:
                print(f'{i[0]:15} rango de precios: {i[1]:3}k a {i[2]:3}k')

        if orden == 2:
            ordenados=CBD.pullDatos(f'SELECT Nombre,Valor_minimo,Valor_maximo FROM Restaurantes ORDER BY Valor_maximo desc, Valor_minimo desc')
            for i in ordenados:
                print(f'{i[0]:15} rango de precios: {i[1]:3}k a {i[2]:3}k')

        if orden == 3:
            return

    if opcion == 3:
        print('------------- TIEMPO PROMEDIO DE ESPERA -------------')
        filtrado=CBD.pullDatos(f'SELECT Nombre, Round(AVG(Tiempo_Espera),2) as Prom, Round(AVG(Tiempo),2)  FROM Calificaciones GROUP BY Nombre ORDER BY Prom desc;')
        for i in filtrado:
            print(f'{i[0]:15} --> {i[1]:3} mins')
    
    if opcion == 4:
        print('---------- CALIFICACION PROMEDIO DE CALIDAD ----------')
        filtrado=CBD.pullDatos(f'SELECT Nombre, Round(AVG(Calidad),2) as Prom FROM Calificaciones GROUP BY Nombre ORDER BY Prom desc;')
        for i in filtrado:
            print(f'{i[0]:15} --> {i[1]:3} ⭐')

    if opcion == 5:
        print('---------- CALIFICACION PROMEDIO DE ATENCIÓN ----------')
        filtrado=CBD.pullDatos(f'SELECT Nombre, Round(AVG(Atencion),2) as Prom FROM Calificaciones GROUP BY Nombre ORDER BY Prom desc;')
        for i in filtrado:
            print(f'{i[0]:15} --> {i[1]:3} ⭐')

    if opcion == 6:
        return

# ---------------------------------------------- CALIFICAR RESTAURANTES Y AGREGARLOS A LA BASE DE DATOS --------------------------------
def calificarR():
    calidad = intLimitado(input('Del 1 al 5 ⭐, ¿Cual es la calidad?\nIngrese la puntuacion de la calidad: \n'),5)
    atencion = intLimitado(input('Del 1 al 5 ⭐, ¿Cual es la atencion?\nIngrese la puntuacion de la atencion ofrecida por el restaurante: \n'),5)
    Tiempo_Espera = intLimitado(input('¿Cuanto tiempo suele esperar para que entreguen la comida? (En minutos): \n'))
    comentario = input('Agregue un comentarios sobre el restaurante: \n')        
    if Tiempo_Espera < 15:
        tiempo = 5
    elif 15 <= Tiempo_Espera and Tiempo_Espera <= 30:
        tiempo = 4
    elif 30 < Tiempo_Espera and Tiempo_Espera <= 45:
        tiempo = 3
    elif 45 < Tiempo_Espera and Tiempo_Espera <= 60:
        tiempo = 2
    elif Tiempo_Espera > 60:
        tiempo = 1
    return calidad,tiempo,atencion,comentario,Tiempo_Espera
          
def calificar_restaurantes():
    print('¿El restaurante esta aqui?: ')
    restaurantes = CBD.pullDatos('SELECT * FROM Restaurantes')
    for i in restaurantes:
        print(f'\t{i[1]:10}')

    while True:
        opcion = intLimitado(input(f'1. Si.\n'
        + '2. No.\n'
        + '3. Regresar.\n'
        + 'Ingrese la opcion que desee: \n'),3,1)
        if opcion == 1:
            print("\n¿Cual restaurante es?")
            for i in restaurantes: 
                print(f'\t{i[0]}) {i[1]:10}')
            seleccion = intLimitado(input('Ingrese el numero del restaurante: \n'),len(restaurantes))
            nombre = CBD.pullDatos(f'SELECT Nombre FROM Restaurantes WHERE ID = {seleccion}')
            calidad,tiempo,atencion,comentario,tiempo_espera=calificarR()            
            elegir = intLimitado(input('\n¿Está seguro de las opciones que eligió?\n'
            + f'Nombre: {nombre[0][0]}, Calidad: {calidad}, Tiempo: {tiempo_espera} mins, Atención: {atencion}\nComentario: {comentario}\n'
            +'1.Si\n'
            +'2.No\n'),2,1)

            if elegir == 1:
                CBD.pushDatos(f'INSERT INTO Calificaciones VALUES ("{nombre[0][0]}",{calidad},{tiempo},{atencion},"{comentario}",{tiempo_espera})')
                return
            else:
                return
            
        elif opcion == 2:
            print("")
            cantidad = CBD.pullDatos('SELECT COUNT(nombre) FROM Restaurantes')
# Esta funcion se encarga de comprobar que el nombre que se va a agregar no se repita en la base de datos, 
# pues esto puede generar error al ser una llave primaria
            def comprobar():
                comprobar = CBD.pullDatos('SELECT nombre FROM Restaurantes')
                while True:
                    comprobador=[]
                    Nombre = ((input('Ingrese el nombre del restaurante: \n')).lower()).capitalize()
                    [comprobador.append(i[0]) for i in comprobar]
                    if Nombre in comprobador:
                        print('El nombre que intenta agregar, se encuentra en la base de datos')
                    else:
                        return Nombre
            Nombre = comprobar()
            Tipo = input('\n¿Que tipo de comida venden?\nIngrese el tipo de comida que venden: \n')
            Direccion = input('\n¿Cual es la direccion?\nIngrese la direccion del restaurante: \n')
            Valor_minimo = intLimitado(input('\n¿Cual es el plato con menor valor?\nIngrese el valor del plato más económico: \n'))
            Valor_maximo = intLimitado(input('\n¿Cual es el plato con mayor valor?\nIngrese el valor del plato más costoso: \n'))
            
            elegir = intLimitado(input('\n¿Está seguro de las opciones que eligió?\n'
            + f'Nombre: {Nombre}, Tipo de comida: {Tipo}, Dirección: {Direccion}, Rango de precios: ({Valor_minimo} - {Valor_maximo})\n'
            +'1.Si\n'
            +'2.No\n'),2,1)

            if elegir == 1:
                CBD.pushDatos(f'INSERT INTO Restaurantes VALUES ("{cantidad[0][0]+1}","{Nombre}","{Tipo}","{Direccion}",{Valor_minimo},{Valor_maximo})')
                calidad,tiempo,atencion,comentario,tiempo_espera=calificarR()            
                elegir = intLimitado(input('\n¿Está seguro de las opciones que eligió?\n'
                + f'Nombre: {Nombre}, Calidad: {calidad}, Tiempo: {tiempo_espera}, Atención: {atencion}\nComentario: {comentario}\n'
                +'1.Si\n'
                +'2.No\n'),2,1)
                if elegir == 1:
                    CBD.pushDatos(f'INSERT INTO Calificaciones VALUES ("{Nombre}",{calidad},{tiempo},{atencion},"{comentario}",{tiempo_espera})')
                    return
                else:
                    return
            else:
                return
        elif opcion == 3:
            return

# ---------------------------------------------------------------------- PROXIMAMENTE, UBICACIONES CON MAPS --------------------------------
def ubicaciones_restaurantes():
    #MOSTRAR MAPA DE LAS UBICACIONES (SEGUN AXEL ES FACIL CON TKINTER)
    pass
# 200 lineas!!!