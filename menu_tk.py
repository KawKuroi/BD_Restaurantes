import funciones as Func
from tkinter import *

archivo = 'lector.txt'
color_01,color_02,color_03,color_04,color_05='#6D9886','#282E35','#F2E7D5','#393E46','#F7F7F7'
# ------------------------------------------------------------------ Creacion de root (El lienzo)
root = Tk()
root.title('Proyecto')
root.iconbitmap('icono.ico')
widthROOT = root.winfo_screenwidth()  
heightROOT = root.winfo_screenheight() 
root.geometry("%dx%d" % (widthROOT, heightROOT))
root.state('zoomed')
root.config(bg='#000000')

# ------------------------------------------------------------------ Creacion de bloques
body = Frame(root,bg=color_01,bd=0)
nav = Frame(root,bg=color_02,bd=0)

def forget():
    global body
    body.place_forget()

# ------------------------------------------------------------------ Creacion de Canva para Scroll lateral

def crearCanva():
    global canva
    global blank
    # CREACION DE CANVA PARA EL SCROLL
    canva = Canvas(body)
    canva.pack(side=LEFT, fill=BOTH, expand=YES)   

    scroll = Scrollbar(body,orient="vertical", command=canva.yview)
    scroll.pack(side=RIGHT, fill=Y)

    canva.configure(yscrollcommand=scroll.set)
    canva.bind('<Configure>',lambda e : canva.configure(scrollregion=canva.bbox('all')))

    # EL FRAME QUE SE VA A USAR

    blank = Frame(canva,bg=color_01,bd=0)
    canva.create_window((0,0),window=blank,width=int(widthROOT*0.85),anchor='nw')

# ------------------------------------------------------------------ OPCION 01

def opcion_01():
    forget() 
    global body
    body = Frame(root,bg=color_01,bd=0)
    body.place(relheight=1,relwidth=0.85,x=widthROOT*0.15)

    crearCanva()

    # INFO DE LA SECCION

    Label(blank, text='INFO RESTAURANTES', font=('Arial 30 bold'), fg=color_03, bg=color_01, pady=50).pack(fill=BOTH)
    Func.info_restaurantes()
    txt = (open(archivo,'r',encoding='utf-8').readlines())

    for i in txt:
        separar=(i.replace('\n','')).split('..')
        print(separar)
        Label(blank, text=f'Restaurante = {separar[0]}', font=('Arial 16'), fg=color_04, bg=color_03, justify='center',pady=15).pack(pady=(18,0),fill=BOTH)
        Label(blank, text=f'Tipo de comida = {separar[1]}\nDirección = {separar[2]}\nRango de precios = {separar[3]} a {separar[4]}', font=('Arial 15'), fg=color_04, bg=color_01, justify='center',pady=10).pack(pady=18,fill=BOTH)

# ------------------------------------------------------------------ OPCION 02

def opcion_02():
    forget()
    global body
    body = Frame(root,bg=color_01,bd=0)
    body.place(relheight=1,relwidth=0.85,x=widthROOT*0.15)

    crearCanva()

    Label(blank, text='CALIFICACIONES', font=('Arial 30 bold'), fg=color_03, bg=color_01, pady=50).pack(fill=BOTH)
    Func.calificaciones_restaurantes()
    txt = (open(archivo,'r',encoding='utf-8').readlines())

    for i in txt:
        separar=(i.replace('\n','')).split('..')
        Label(blank, text=f'Restaurante = {separar[0]}, Calificacion ⭐ = {separar[1]}, Comentarios =', font=('Arial 16 '),  fg=color_04, bg=color_03, justify='left',pady=15).pack(pady=18,fill=BOTH)
        a=((((separar[2].replace("['",'')).replace("]'",'')).replace("'",'')).replace("]",'')).split(',')
        print(a)
        for i in a:
            Label(blank, text=f'- {i}', font=('Arial 15'), fg=color_04, bg=color_01, justify='left').pack(pady=10, side=TOP)  

# ------------------------------------------------------------------ OPCION 03

opFiltros = ['Tipo de comida','Rango de precio','Tiempos de espera promedio','Calificación promedio de calidad','Calificación promedio de atención']

def opcion_03():
    forget() 
    global body
    body = Frame(root,bg=color_01,bd=0)
    body.place(relheight=1,relwidth=0.85,x=widthROOT*0.15)

    Label(body, text='FILTROS', font=('Arial 30 bold'), fg=color_03, bg=color_01, pady=50).pack(fill=BOTH)
    Label(body, text='Seleccione una opción para filtrar', font=('Arial 17 bold'), fg=color_04, bg=color_03, pady=10).pack(fill=BOTH)
    
    clicked = StringVar()
    clicked.set(opFiltros[0])

    drop = OptionMenu(body, clicked, *opFiltros)
    drop.config(bd=0,padx=50, pady=10, font=('Arial 15'), bg=color_03, fg=color_04, activeforeground=color_04)
    drop.pack()

    opcion = int(opFiltros.index(clicked.get())+1)
    Func.filtros(opcion)

    if opcion == 1:
        try:
            canva.pack_forget()
        except:
            pass
        crearCanva()
        Label(blank, text='Seleccione una opción', font=('Arial 17 bold'), fg=color_03, bg=color_01, pady=10).pack(fill=BOTH)
        txt = (open(archivo,'r',encoding='utf-8').readlines()) 
        nOpcion=[]
        for i in txt:
            nOpcion.append(i.replace('\n',''))

        clicked = StringVar()
        clicked.set(nOpcion[0])

        Func.filtros(opcion,nOpcion.index(clicked.get())+1)
        drop = OptionMenu(blank, clicked, *nOpcion)
        drop.config(bd=0,padx=50, pady=10, font=('Arial 15'), bg=color_03, fg=color_04, activeforeground=color_04)
        drop.pack()
    body.update()   


# ------------------------------------------------------------------ OPCION 04

def opcion_04():
    forget()
    body = Frame(root,bg=color_01,bd=0)
    body.place(relheight=1,relwidth=0.85,x=widthROOT*0.15)

    canva = Canvas(body)
    canva.pack(side=LEFT, fill=BOTH, expand=YES)   

    scroll = Scrollbar(body,orient="vertical", command=canva.yview)
    scroll.pack(side=RIGHT, fill=Y)

    canva.configure(yscrollcommand=scroll.set)
    canva.bind('<Configure>',lambda e : canva.configure(scrollregion=canva.bbox('all')))

    # EL FRAME QUE SE VA A USAR

    blank = Frame(canva,bg=color_01,bd=0)
    canva.create_window((0,0),window=blank,width=int(widthROOT*0.85),anchor='nw')

    def send():
        nombreV,tipoV,dirV,minV,maxV,CalidadV,AtencionV,EsperaV,ComentarioV=nombre.get(),tipo.get(),dir.get(),min.get(),max.get(),Calidad.get(),Atencion.get(),Espera.get(),Comentario.get()
        
        if not nombreV or not tipoV or not dirV or not minV or not maxV or not CalidadV or not AtencionV or not EsperaV or not ComentarioV:
            print('Error, hay espacios sin llenar')
        else:
            try:
                minV=int(minV)
                maxV=int(maxV)
                CalidadV=int(CalidadV)
                AtencionV=int(AtencionV)
                EsperaV=int(EsperaV)

                print((nombreV.lower()).capitalize(),(tipoV.lower()).capitalize(),(dirV.lower()).capitalize(),minV,maxV,CalidadV,tiempo,AtencionV,ComentarioV,EsperaV)  
                if EsperaV < 0 and EsperaV < 15:
                    tiempo = 5
                elif 15 <= EsperaV and EsperaV <= 30:
                    tiempo = 4
                elif 30 < EsperaV and EsperaV <= 45:
                    tiempo = 3
                elif 45 < EsperaV and EsperaV <= 60:
                    tiempo = 2
                elif EsperaV > 60:
                    tiempo = 1

                Func.agregar_restaurante((nombreV.lower()).capitalize(),(tipoV.lower()).capitalize(),(dirV.lower()).capitalize(),minV,maxV)
                Func.agregar_calificacion((nombreV.lower()).capitalize(),CalidadV,tiempo,AtencionV,ComentarioV,EsperaV)

                nombre.delete(0,END)
                tipo.delete(0,END)
                dir.delete(0,END)
                min.delete(0,END)
                max.delete(0,END)
                Calidad.delete(0,END)
                Atencion.delete(0,END)
                Espera.delete(0,END)
                Comentario.delete(0,END)                    

            except Exception as e:
                print('Numero fuera de rango',e)
            except:
                print('Error, intenta colocar letras donde debe ir numeros')
            

        
    Label(blank, text='AGREGAR UN RESTAURANTE', font=('Arial 30 bold'), fg=color_03, bg=color_01, pady=50).pack(fill=BOTH)
    
    Label(blank, text='Nombre del restaurante',fg=color_03,bg=color_01,font=('Arial 17 bold'),pady=15).pack()
    nombre = Entry(blank, width=50,bd=0,font=('Arial 14'),bg=color_05,fg=color_04)
    nombre.pack()
    
    Label(blank, text='Tipo de comida',fg=color_03,bg=color_01,font=('Arial 17 bold'),pady=15).pack()
    tipo = Entry(blank, width=50,bd=0,font=('Arial 14'),bg=color_05,fg=color_04)
    tipo.pack()

    Label(blank, text='Direccion',fg=color_03,bg=color_01,font=('Arial 17 bold'),pady=15).pack()
    dir = Entry(blank, width=50,bd=0,font=('Arial 14'),bg=color_05,fg=color_04)
    dir.pack()
    
    Label(blank, text='Valor minimo (miles de pesos)',fg=color_03,bg=color_01,font=('Arial 17 bold'),pady=15).pack()
    min = Entry(blank, width=50,bd=0,font=('Arial 14'),bg=color_05,fg=color_04)
    min.pack()

    Label(blank, text='Valor máximo (miles de pesos)',fg=color_03,bg=color_01,font=('Arial 17 bold'),pady=15).pack()
    max = Entry(blank, width=50,bd=0,font=('Arial 14'),bg=color_05,fg=color_04)
    max.pack()

    # ---------------------------------------------------------------------- CALIFICACIONES 

    Label(blank, text='Calificacion de Calidad (1 al 5)',fg=color_03,bg=color_01,font=('Arial 17 bold'),pady=15).pack()
    Calidad = Entry(blank, width=50,bd=0,font=('Arial 14'),bg=color_05,fg=color_04)
    Calidad.pack()

    Label(blank, text='Calificacion de Atención (1 al 5)',fg=color_03,bg=color_01,font=('Arial 17 bold'),pady=15).pack()
    Atencion= Entry(blank, width=50,bd=0,font=('Arial 14'),bg=color_05,fg=color_04)
    Atencion.pack()

    Label(blank, text='Tiempo de espera aproximado (minutos)',fg=color_03,bg=color_01,font=('Arial 17 bold'),pady=15).pack()
    Espera = Entry(blank, width=50,bd=0,font=('Arial 14'),bg=color_05,fg=color_04)
    Espera.pack()

    Label(blank, text='¡Agregue un comentario!',fg=color_03,bg=color_01,font=('Arial 17 bold'),pady=15).pack()
    Comentario = Entry(blank, width=50,bd=0,font=('Arial 14'),bg=color_05,fg=color_04)
    Comentario.pack()

    void = Label(blank, text='', height=2,bg=color_01).pack()
    
    Button(blank, text = 'Enviar', command=send,pady=15, padx=15, bd=0,fg=color_03,bg=color_02,font=('Arial 14 bold')).pack()

def opcion_05():
    pass


# ------------------------------------------------------------------ NAV
Label(nav, pady=35, text='Opciones',bd=0, font=('Arial 14 bold'), fg=color_03, bg=color_02).pack(fill='x',pady=2)
Button(nav, pady=35, text='Información\n de Restaurantes',bd=0, font=('Arial 14 bold'), fg=color_03, bg=color_04, command=opcion_01).pack(fill='x',pady=2)
Button(nav, pady=35, text='Calificaciones\n de Restaurantes',bd=0, font=('Arial 14 bold'), fg=color_03, bg=color_04, command=opcion_02).pack(fill='x',pady=2)
Button(nav, pady=35, text='Filtros\n de Restaurantes',bd=0, font=('Arial 14 bold'), fg=color_03, bg=color_04, command=opcion_03).pack(fill='x',pady=2)
Button(nav, pady=35, text='Agregar\n Restaurante',bd=0, font=('Arial 14 bold'), fg=color_03, bg=color_04, command=opcion_04).pack(fill='x',pady=2)
Button(nav, pady=35, text='Calificar\n Restaurante',bd=0, font=('Arial 14 bold'), fg=color_03, bg=color_04, command=opcion_05).pack(fill='x',pady=2)
Button(nav, pady=35, text='Salir\n del programa',bd=0, font=('Arial 14 bold'), fg=color_03, bg=color_04,command= root.quit).pack(fill='x',pady=2,side='bottom')


# ------------------------------------------------------------------ BODY

Label(body, text='Bienvenid@ al programa!!!! :)', font=('Arial 25 bold'), fg=color_03, bg=color_01).pack(fill=BOTH,expand=YES)

# Tienen que cargar de ultimas !!!
root.update()
body.place(relheight=1,relwidth=0.85,x=widthROOT*0.15)
nav.place(relheight=1,relwidth=0.15)
root.mainloop()