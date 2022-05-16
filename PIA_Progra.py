from datetime import datetime
import sqlite3
from sqlite3 import Error
import sys
from xmlrpc.client import DateTime


while True:
    
    print(" ")
    print("-"*50)
    print("MENÚ PRINCIPAL - Reparacion de computadoras y aparatos diversos")
    print("-"*50)
    print("[r] Registrar un servicio")
    print("[c] Consultar un servicio")
    print("[s] Consultar servicio en fecha especificada")
    print("[x] Salir")
    opcion=input("Qué opción deseas: ")
    if (opcion=="x"):
        break
    if (opcion=="r"):
        try:
            with sqlite3.connect("EVIDENCIA_3.db") as conn:
                mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS proyecto (_FOLIO INTEGER NOT NULL PRIMARY KEY, _FECHA TEXT NOT NULL, _MONTO INTEGER NOT NULL, _SERVICIO TEXT NOT NULL, _TOTAL REAL);")
            print("Tabla creada exitosamente")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            _FOLIO= int(input("digite el folio: "))
            _FECHA=(input("digite la fecha dd/mm/aaaa : "))
            _MONTO= int(input("digite el monto a pagar: "))
            _SERVICIO= input("digite el  servicio: ")
            iva = 1.16
            _TOTAL= (_MONTO*iva)
            mi_cursor.execute("INSERT INTO proyecto VALUES("(_FOLIO))
            mi_cursor.execute("INSERT INTO proyecto VALUES("(_FECHA))
            mi_cursor.execute("INSERT INTO proyecto VALUES("(_MONTO))
            mi_cursor.execute("INSERT INTO proyecto VALUES("(_SERVICIO))
            mi_cursor.execute("INSERT INTO proyecto VALUES("(_TOTAL))
            conn.close()
            print("datos agregados correctamente")

    if (opcion=="c"):
        input("digite el folio a buscar: ")
        contador= -1
        indice= -1
        for var in _FOLIO:
            contador= contador+1
            if (var._FOLIO== True):
                indice=contador
                break
             
            if (not _FOLIO== ""):
                print("no se encontraron coincidencias")

    if (opcion=="s"):
         input("digite la fecha a buscar: ")
         contador= -1
         indice= -1
         for var in _FECHA:
            contador= contador+1
            if (var._FECHA== True):
                indice=contador
                break
             
            if (not _FECHA== ""):
                print("no se encontraron coincidencias")
