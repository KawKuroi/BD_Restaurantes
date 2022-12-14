import Comandos_baseDatos as CBD
from cmath import inf
archivo = 'lector.txt'
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
    txt = open(archivo,'w')
    txt = open(archivo,mode ='a',encoding='utf-8')
    print('----------- INFO RESTAURANTES --------------')
    restaurantes = CBD.pullDatos('SELECT * FROM Restaurantes')
    for i in restaurantes:
        txt.writelines([str(i[1]),'..',str(i[2]),'..',str(i[3]),'..',str(i[4]),'..',str(i[5]),'\n'])

# -------------------------------------------------- MOSTRANDO INFORMACION GENERAL DE CALIFICACIONES --------------------------------
def calificaciones_restaurantes():
    txt = open(archivo,'w')
    txt = open(archivo,mode ='a',encoding='utf-8')
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
        l=[]
        for x in i['comentarios']:
            l.append(x)
        txt.writelines([str(i['nombre']),'..',str(i['nota']),'..',str(l),'\n'])

# ------------------------------------- FILTROS PARA LA BASE DE DATOS, RESTAURANTES Y CALIFICACIONES --------------------------------
def filtros(opcion,selec=0):
    if opcion == 1:
        txt = open(archivo,'w')
        txt = open(archivo,mode ='a',encoding='utf-8')
        Tipo=CBD.pullDatos('SELECT Tipo FROM Restaurantes GROUP BY Tipo')
        posiciones={}
        print('Seleccione el un tipo de comida para filtrar restaurantes')
        for x,i in enumerate(Tipo,1):
            txt.writelines([str(i[0]),'\n'])
            posiciones[x]=i[0]

        if selec != 0:
            for pos,tipo in posiciones.items():
                if selec == pos:
                    filtrados=CBD.pullDatos(f'SELECT Nombre FROM Restaurantes WHERE Tipo = "{tipo}"')                
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

def agregar_restaurante(Nombre,Tipo,Direccion,Valor_minimo,Valor_maximo): 
    cantidad = CBD.pullDatos('SELECT COUNT(nombre) FROM Restaurantes')
    CBD.pushDatos(f'INSERT INTO Restaurantes VALUES ("{cantidad[0][0]+1}","{Nombre}","{Tipo}","{Direccion}",{Valor_minimo},{Valor_maximo})')

def agregar_calificacion(Nombre,calidad,tiempo,atencion,comentario,tiempo_espera):
    CBD.pushDatos(f'INSERT INTO Calificaciones VALUES ("{Nombre}",{calidad},{tiempo},{atencion},"{comentario}",{tiempo_espera})')

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