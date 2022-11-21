import funciones as Func
from tkinter import *

archivo = 'lector.txt'

# ------------------------------------------------------------------ Creacion de root (El lienzo)
root = Tk()
root.title('Proyecto')
root.iconbitmap('icono.ico')
widthROOT = root.winfo_screenwidth()  
heightROOT = root.winfo_screenheight() 
root.geometry("%dx%d" % (widthROOT, heightROOT)) 
root.config(bg='#000000')

# ------------------------------------------------------------------ Creacion de bloques
body = Frame(root,bg='#6D9886',bd=0)
nav = Frame(root,bg='#282E35',bd=0)

def forget():
    global body
    body.place_forget()
    
# ------------------------------------------------------------------ OPCION 01
def opcion_01():
    forget() 
    global body
    body = Frame(root,bg='#6D9886',bd=0)
    Scrollbar(body,orient="vertical").pack(side="right",fill="y")
    Label(body, text='INFO RESTAURANTES', font=('Arial 20 bold'), fg='#F2E7D5', bg='#6D9886', pady=20).pack(fill=BOTH)
    Func.info_restaurantes()
    txt = (open(archivo,'r',encoding='utf-8').readlines())
    for i in txt:
        separar=(i.replace('\n','')).split('..')
        print(separar)
        Label(body, text=f'Restaurante = {separar[0]}\n\tTipo de comida = {separar[1]}\n\tDirección = {separar[2]}\n\tRango de precios = {separar[3]} a {separar[4]}', font=('Arial 15'), fg='#F7F7F7', bg='#6D9886', justify='left').pack(pady=10, side=TOP)
    for i in range(0, 100):
        Label(body, text='HOLA').pack()
    body.place(relheight=1,relwidth=0.85,x=widthROOT*0.15)

# ------------------------------------------------------------------ OPCION 02

def opcion_02():
    forget()
    global body
    body = Frame(root,bg='#6D9886',bd=0)
    Scrollbar(body,orient="vertical").pack(side="right",fill="y")
    Label(body, text='CALIFICACIONES', font=('Arial 20 bold'), fg='#F2E7D5', bg='#6D9886', pady=20).pack(fill=BOTH)
    Func.calificaciones_restaurantes()
    txt = (open(archivo,'r',encoding='utf-8').readlines())
    for i in txt:
        separar=(i.replace('\n','')).split('..')
        Label(body, text=f'Restaurante = {separar[0]}, Calificacion ⭐ = {separar[1]}, Comentarios =', font=('Arial 15'), fg='#F7F7F7', bg='#6D9886', justify='left').pack(pady=10, side=TOP)
        a=((((separar[2].replace("['",'')).replace("]'",'')).replace("'",'')).replace("]",'')).split(',')
        print(a)
        for i in a:
            Label(body, text=f'- {i}', font=('Arial 15'), fg='#F7F7F7', bg='#6D9886', justify='left').pack(pady=10, side=TOP)
        Label(body, text=f'\n',bg='#6D9886').pack()
    body.place(relheight=1,relwidth=0.85,x=widthROOT*0.15)

# ------------------------------------------------------------------ OPCION 03

def opcion_03():
    forget()
    body = Frame(root,bg='#6D9886',bd=0)
    body.place(relheight=1,relwidth=0.85,x=widthROOT*0.15)

# ------------------------------------------------------------------ OPCION 04

def opcion_04():
    forget()
    body = Frame(root,bg='#6D9886',bd=0)
    body.place(relheight=1,relwidth=0.85,x=widthROOT*0.15)


# ------------------------------------------------------------------ NAV

Button(nav, pady=35, text='Información\n de Restaurantes',bd=0, font=('Arial 14 bold'), fg='#F7F7F7', bg='#393E46', command=opcion_01).pack(fill='x',pady=2)
Button(nav, pady=35, text='Calificaciones\n de Restaurantes',bd=0, font=('Arial 14 bold'), fg='#F7F7F7', bg='#393E46', command=opcion_02).pack(fill='x',pady=2)
Button(nav, pady=35, text='Filtros\n de Restaurantes',bd=0, font=('Arial 14 bold'), fg='#F7F7F7', bg='#393E46', command=opcion_03).pack(fill='x',pady=2)
Button(nav, pady=35, text='Calificar\n Restaurantes',bd=0, font=('Arial 14 bold'), fg='#F7F7F7', bg='#393E46', command=opcion_04).pack(fill='x',pady=2)
Button(nav, pady=35, text='Salir\n del programa',bd=0, font=('Arial 14 bold'), fg='#F7F7F7', bg='#393E46',command= root.quit).pack(fill='x',pady=2,side='bottom')


# ------------------------------------------------------------------ BODY

Label(body, text='Bienvenid@ al programa!!!! :)', font=('Arial 25 bold'), fg='#F2E7D5', bg='#6D9886').pack(fill=BOTH,expand=YES)

# Tienen que cargar de ultimas !!!
root.update()
body.place(relheight=1,relwidth=0.85,x=widthROOT*0.15)
nav.place(relheight=1,relwidth=0.15)
root.mainloop()