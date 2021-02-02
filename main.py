"""
Proyecto Python MySQL:
-Abrir asistente
-Login o Registro
|-Registro: Creara un usuario en la base de datos.
|-Login: identificara al usuario y no dara más opciones.
#Crear notas, mostrar notas, borrar notas.
"""
from usuarios import acciones #import usuarios.acciones



######################### Menu inicial
def menuinical():
    print("""
    ########### ACCIONES DISPONIBLES:   ###########
    *   registro
    *   login
    *   salir
    """)
    inicia = acciones.Acciones()
    while True:
        accion = input("¿Qué quieres hacer?:    ").lower()

        if accion == 'registro':
            inicia.registro()
        elif accion == 'login':
            inicia.login()
        elif accion == 'salir':
            break
        else:
            print("Solo puede hacer login, registro o salir ...")

menuinical()