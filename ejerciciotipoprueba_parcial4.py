#ejercicio1
#haga un programa que genere un menu de ingreso de usuario
#el menu principal debe permitir mostrar 3 opcciones principales
#1- ingresar usuario
#2_ buscar usuario
#3- eliminar usuario
#4- continuar ingresando usuario o salir

# al ingresar al opccion 1 se debe permitir ingresar el nombre del usuario, sexo y clave por separado
# para que le ingreso del usuario sea exitoso se debe compartir lo siguiente, 1- el nombre del usuario no debe estar repetido
# el sexo del usuario debe ser definido a traves de dos letras F o M
# la contraseña debe ser de un minimo de 8 caracteres, debe tener al menos 1 numero, debe tener a menos una letra y no debe tener espacios
# en caso de cumplir todas las condiciones, el mensaje a demostrar en pantalla ingreso exitoso

#opcion 2: el mnenu debeb cumpliar al buscar los usuarios mediante el nombre del usuario, 
# si el usuario existe deben mostarse los datos asociados(sexo y contraseña)
# si el usuario no existe debe mostrar un mensaje el usuario no se encuentra registrado

#opcion3: el menu debe permitir eliminar usuarios y toda su informacion asociada a este

#opcion4: dar la opccion de agregar otro usuario o salir

# recomendacion: si el ingreso de una opccion distinta, debe mostrar un mensaje que debe seleccionar una opccion valida
# todas las opcciones del menu deben estar implementadas con funciones separadas del codigo principal, (main)
# Función para validar si la contraseña cumple los requisitos
def validar_contraseña(clave):
    if len(clave) < 8:
        return False
    if " " in clave:
        return False
    tiene_numero = any(char.isdigit() for char in clave)
    tiene_letra = any(char.isalpha() for char in clave)
    return tiene_numero and tiene_letra

# Función para ingresar usuario
def ingresar_usuario(usuarios):
    nombre = input("Ingrese el nombre del usuario: ").strip()
    # Validar nombre no repetido
    if nombre in usuarios:
        print("El nombre de usuario ya existe. Intente con otro.")
        return

    sexo = input("Ingrese el sexo (F/M): ").strip().upper()
    if sexo not in ["F", "M"]:
        print("Sexo inválido. Debe ser 'F' o 'M'.")
        return

    clave = input("Ingrese la contraseña: ")
    if not validar_contraseña(clave):
        print("Contraseña inválida. Debe tener mínimo 8 caracteres, al menos un número, una letra y no contener espacios.")
        return

    # Si todo OK, guardar usuario
    usuarios[nombre] = {"sexo": sexo, "clave": clave}
    print("Ingreso exitoso.")

# Función para buscar usuario
def buscar_usuario(usuarios):
    nombre = input("Ingrese el nombre del usuario a buscar: ").strip()
    if nombre in usuarios:
        datos = usuarios[nombre]
        print(f"Usuario: {nombre}")
        print(f"Sexo: {datos['sexo']}")
        print(f"Contraseña: {datos['clave']}")
    else:
        print("El usuario no se encuentra registrado.")

# Función para eliminar usuario
def eliminar_usuario(usuarios):
    nombre = input("Ingrese el nombre del usuario a eliminar: ").strip()
    if nombre in usuarios:
        del usuarios[nombre]
        print(f"Usuario '{nombre}' eliminado correctamente.")
    else:
        print("El usuario no se encuentra registrado.")

# Función principal (main)
def main():
    usuarios = {}
    while True:
        print("\n--- Menú Principal ---")
        print("1 - Ingresar usuario")
        print("2 - Buscar usuario")
        print("3 - Eliminar usuario")
        print("4 - Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ingresar_usuario(usuarios)
        elif opcion == "2":
            buscar_usuario(usuarios)
        elif opcion == "3":
            eliminar_usuario(usuarios)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Debe seleccionar una opción válida.")

        if opcion != "4":
            continuar = input("¿Desea realizar otra acción? (s/n): ").strip().lower()
            if continuar != "s":
                print("Saliendo del programa.")
                break

if __name__ == "__main__":
    main()
