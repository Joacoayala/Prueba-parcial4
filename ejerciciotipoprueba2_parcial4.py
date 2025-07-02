#ejercicio2 listas, diccionarios, funciones

#realize un programa que permita generar un menu de gestion de entradas para el concierto de noche de brujas
# el menu principal debe permitir mostrar 4 opciones

# MENU PRINCIPAL
# opcion 1) comprar entradas - (se debe permitir ingresar el nombre del comprador, tipo de entrada y codigo de confirmacion por separado, 
# para que la compra sea exitosa se debe cumplir: el nombre del comprador no debe repetirse, el tipo de entrada debe ser general o vip, general tiene un costo de 10.000 y vip 50.000, 
# el codigo de confirmacion debe tener un minimo de 6 caracteres y que tenga una mayuscula, una minuscula y un numero y no debe haber espacios, 
# si se cumplen todas las condiciones se muestra "entrada comprada con exito")


# opcion 2) consultar comprador - (el menu debe permitir buscar compradores mediante el nombre,
# si el comprador existe debe mostarse los datos asociados a este como por ejemplo, 
# nombre, tipo de entrada y valor de ella y codigo de confirmacion, si no existe el usuario se muestra, usuario no encontrado)


# opcion 3) cancelar compra - (el menu debe permitir o mostrar la opccion de elimininar el comprador con toda su informacion asociada)


# opcion 4) - desea utilizar otra opccion o salir (consultarle al usuario si desea realizar otra opcion o salir del programa)

#todas las opcciones del menu deben estar implementadas dentro de funciones separadas del codigo principal (main)
def menu_ventas():
    General = 10000
    Vip = 50000
    while True:
        print("**** MENU VENTA DE ENTRADAS ****")
        print("[1]- Comprar entradas")
        print("[2]- Consultar comprador")
        print("[3]- Cancelar compra")
        print("[4]- Salir")
menu_ventas()            

def compra_de_entradas():
    opcion_menu = input("ingresa una opccion del menu: ")
    if opcion_menu == "1":
        print("Tenemos dos tipos de entradas disponibles - General $10.000 y Vip $50.000")
        tipo_entrada = input("ingrese el tipo de entrada a comprar: ").lower(tipo_entrada)
    if tipo not in ["general", "vip"]:
        print("Tipo de entrada inválido.")
        return

    if tipo == "general":
        valor = 10000
    else:
        valor = 50000

    codigo = input("Ingrese el código de confirmación: ")
    if not validar_codigo(codigo):
        print("Código inválido. Debe tener mínimo 6 caracteres, una mayúscula, una minúscula, un número y sin espacios.")
        return

    compradores[nombre] = {
        "tipo": tipo,
        "valor": valor,
        "codigo": codigo
    }
    print(" Entrada comprada con éxito.")


def consultar_comprador():
    nombre = input("Ingrese el nombre del comprador a buscar: ")
    if nombre in compradores:
        datos = compradores[nombre]
        print(f"\nComprador encontrado:\nNombre: {nombre}\nTipo de entrada: {datos['tipo']}\nValor: {datos['valor']}\nCódigo: {datos['codigo']}")
    else:
        print(" Usuario no encontrado.")


def cancelar_compra():
    nombre = input("Ingrese el nombre del comprador a eliminar: ")
    if nombre in compradores:
        del compradores[nombre]
        print("Compra cancelada exitosamente.")
    else:
        print("Usuario no encontrado.")


def main():
    while True:
        print("\nMENU PRINCIPAL")
        print("1) Comprar entradas")
        print("2) Consultar comprador")
        print("3) Cancelar compra")
        print("4) Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            comprar_entrada()
        elif opcion == "2":
            consultar_comprador()
        elif opcion == "3":
            cancelar_compra()
        elif opcion == "4":
            salir = input("¿Desea realizar otra operación? (s/n): ").lower()
            if salir != "s":
                print("👋 Gracias por usar el sistema. ¡Hasta luego!")
                break
        else:
            print("Opción inválida. Intente nuevamente.")


main()
        
        
        
            
        
        
    
    
