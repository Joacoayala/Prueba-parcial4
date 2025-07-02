#Ejercicio: Gestión de Usuarios en una Aplicación
#Enunciado:

#Estás desarrollando un pequeño sistema de administración de usuarios para una aplicación. 
# El objetivo es permitir que el usuario pueda:

#Ingresar nuevos usuarios. 1

#Buscar usuarios existentes. 2

#Eliminar usuarios del sistema. 3

#Salir del programa. 4

#Cada usuario debe tener:

#Un nombre único.

#Un sexo que debe ser "M" (masculino) o "F" (femenino).

#Una contraseña válida, que cumpla con los siguientes requisitos:

#Al menos 8 caracteres.

#No debe contener espacios.

#Debe contener al menos una letra y un número.

#El programa principal debe mostrar un menú con las opciones mencionadas y actuar en consecuencia. 

# Usa un diccionario llamado d para almacenar los usuarios

registro = {}
def ingresar_usuario():
    while True:
        nombre = input("ingresa el nombre del usuario: ")
        if nombre not in registro:
            break
        else:
            print("el nombre ingresado ya esta registrado, intente con otro")
            
    while True:
        sexo = input("ingrese el sexo del usuario, M (masculino) o F (femenino): ").upper()
        if sexo == "M" or sexo == "F":
            break
        else:
            print("ingrese una opcion valida, M o F")
            
    while True:
        num = 0
        letras = 0
        contraseña = input("crea una contraseña para el usuario, debe tener minimo 8 caracteres incluyendo una letra y un numero: ")
        if len(contraseña) >= 8 and " " not in contraseña:
            for i in contraseña:
                if i.isdigit():
                    num += 1
                if i.isalpha():
                    letras += 1
                else:
                    print("la contraseña debe contener minimo 8 caracteres y sin espacios")
                if num > 0 and letras > 0:
                    print("contraseña valida")
                    registro[nombre] = [sexo, contraseña]
                    print("usuario registrado con exito")
                    break
                else:
                    print("la contraseña debe contener una letra y un numero")
def buscar_usuario(nombre):
    if nombre in registro:
        print("el sexo del usuario es:", registro[nombre] [1], "y la contraseña es:",[nombre] [0])
    else:
        print("el usuario no se encuentra")
        
def eliminar_usuario(nombre):
    if nombre in registro:
        del d[nombre]
    else:
        print("el usuario ingresado no existe")
        

while True:
    print("*** MENU ***")
    print("[1]- ingresar usuario")
    print("[2]- Buscar usuario")
    print("[3]- Eliminar usuarios")
    print("[4]- Salir del programa")
    
    opcion = input("ingresa una opccion del menu: ")
    if opcion == "1":
        ingresar_usuario()
    elif opcion == "2":
        buscar_usuario()
    elif opcion == "3":
        eliminar_usuario()
    elif opcion == "4":
        print("menu finalizado")
        break
    
    
    
        
    
            
    
