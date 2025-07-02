
d = {}


def ingresar_usuario():
    while True:
        user = input("Ingrese nombre de usuario: ")
        if user not in d:
            break
        else:
            print("Usuario ya existe. Intente otro.")

    while True:
        sex = input("Ingrese sexo (M/F): ").upper()
        if sex == "M" or sex == "F":
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")

    while True:
        num = 0
        letra = 0
        passw = input("Ingrese contraseña: ")
        
        if len(passw) >= 8 and " " not in passw:
            for c in passw:
                if c.isdigit():
                    num += 1
                if c.isalpha():
                    letra += 1

            if num > 0 and letra > 0:
                print("Contraseña válida.")
                d[user] = [passw, sex]
                print("Usuario ingresado con éxito!!")
                break
            else:
                print("La contraseña debe tener letras y números.")
        else:
            print("Contraseña no válida. Debe tener al menos 8 caracteres y sin espacios.")


def buscar_usuario(user):
    if user in d:
        print("El sexo del usuario es:", d[user][1], "y la contraseña es:", d[user][0])
    else:
        print("El usuario no se encuentra.")


def eliminar_usuario(user):
    if user in d:
        del d[user]
        print("Usuario eliminado correctamente.")
    else:
        print("No se pudo eliminar. El usuario no existe.")


while True:
    print("\nMENU PRINCIPAL")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")
    
    op = input("Ingrese opción: ")

    if op == "4":
        print("Programa terminado...")
        break
    elif op == "1":
        ingresar_usuario()
    elif op == "2":
        usuario = input("Ingrese usuario a buscar: ")
        buscar_usuario(usuario)
    elif op == "3":
        usuario = input("Ingrese usuario a eliminar: ")
        eliminar_usuario(usuario)
    else:
        print("Debe ingresar una opción válida!!")

