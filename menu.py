import funciones as Func

def main():
    while True:
        opcion=Func.intLimitado(input("--------------------------------------------\n"
        + "1. Ver informacion acerca de los restaurantes.\n"
        + "2. Ver las calificaciones acerca de los resturantes.\n"
        + "3. Filtros de restaurantes.\n"
        + "4. Calificar restaurantes.\n"
        + "5. Salir del programa.\n"
        + "Ingrese la opcion que desee:\n"),6,1)

        if opcion == 1:
            Func.info_restaurantes()
        
        elif opcion == 2:
            Func.calificaciones_restaurantes()
        
        elif opcion == 3:
            Func.filtros()
        
        elif opcion == 4:
            Func.calificar_restaurantes()
        
        elif opcion == 5    :
            quit("Gracias por usar el programa.")

if __name__ == "__main__":
    main()