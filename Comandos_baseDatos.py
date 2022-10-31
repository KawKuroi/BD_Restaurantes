import sqlite3 as sql

def crearBaseDatos():
    conexion = sql.connect ('Base_Datos.db') # se conecta a la base de datos
    conexion.commit() # Comprueba cambios o crear el archivo
    conexion.close()

def crearTablaRestaurante():
    conexion = sql.connect ('Base_Datos.db')
    cursor = conexion.cursor()
    # La accion que se realizará en la base de datos
    # En este caso se ingresa el nombre de la tabla y luego los valores que va a recibir
    cursor.execute( 
        """
        CREATE TABLE Restaurantes(
            ID int,
            Nombre text,
            Tipo de comida text,
            Direccion text,
            Valor_minimo int,
            Valor_maximo int,
            primary key (ID)
        );
        """
    )
    conexion.commit()
    conexion.close()

def crearTablaCalificaciones():
    conexion = sql.connect ('Base_Datos.db')
    cursor = conexion.cursor()
    cursor.execute( 
        """
        CREATE TABLE Calificaciones(
            Nombre text,
            Calidad int,
            Tiempo de espera int,
            Atencion int,
            Comentarios text,
            foreign key (Nombre) references Restaurantes
        );
        """
    )
    conexion.commit()
    conexion.close()


def pushDatos(instruccion):
    conexion = sql.connect ('Base_Datos.db')
    cursor = conexion.cursor()
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()

def pullDatos(instruccion):
    conexion = sql.connect ('Base_Datos.db')
    cursor = conexion.cursor()
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return datos

if __name__ == '__main__':

# CREACION DE TABLA Y BASE DE DATOS

    #crearBaseDatos()
    #crearTablaRestaurante()
    #pushDatos('drop table calificaciones')
    #crearTablaCalificaciones()
    
    
# MODIFICAR COLUMNAS 

    #pushDatos('alter table Restaurantes drop Valor_maximo')
    #pushDatos('alter table Restaurantes add Valor_maximo')
    #pushDatos('alter table Calificaciones drop Calificacion_prom')
    #pushDatos('alter table Calificaciones add Tiempo_Espera int(4)')
    
# ELIMINAR TODOS LOS DATOS  
    #pushDatos('DELETE FROM Restaurantes')
    #pushDatos('DELETE FROM Calificaciones')

# AGREGANDO DATOS

    # Restaurantes = ID (int), Nombre (txt), Tiempo de comida (txt), Direccion (txt), Valor_maximo (int), Valor_minimo (int)
    #pushDatos('insert into Restaurantes values (2,"KFC","Comida Rapida","por ahí",20,100)')
    
    # Calificaciones = Nombre (txt), calidad (int), tiempo de espera (int), Atencion (int), Comentarios (txt)
    #pushDatos('insert into Calificaciones values ("Presto",4,2,3,"Tiene buenos combos")')
    
# MODIFICAR DATOS
    #pushDatos('update Calificaciones set Tiempo_Espera = 10 where Comentarios = "Pura carne de perro"')

# TOMAR DATOS
    #print(pullDatos('SELECT * from Restaurantes'))
    #print(pullDatos('SELECT * from Calificaciones'))
    
    pass