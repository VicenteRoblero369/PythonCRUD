import pyodbc

def conectar_bd():
    conexion = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-383QDA8;'
        'DATABASE=Empleado;'
        'Trusted_Connection=yes;'

    )
    return conexion