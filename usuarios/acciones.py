import usuarios.usuario as modelo
#from usuarios import usuario as modelo
#import usuario as modelo


class Acciones:
    ######################### Registrar Usuario
    def registro(self):
        print("\nOk, iniciemos con el registro. !!!")
        nombre=input("Dame tu nombre:   ")
        apellidos=input("Dame tus apellidos:   ")
        email=input("Dame tu correo:   ")
        password=input("Dame una contraseña:   ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} has sido registrado con el email: {registro[1].email}")
        else:
            print("No te has registrado corrctamente...")

    ######################### Iniciar sesion
    def login(self):
        print("\nOk, iniciemos sesion. !!!")
        email=input("Dame tu correo:   ")
        password=input("Dame una contraseña:   ")
