#la empresa samsumg necesita realizar el directorio de su ultimo telefono
#el cual maneja el lenguaje python
#nos solicita que esta aplicaccion almacene el nombre, el apellido, direccion, fecha de cumpleaños, y una nota de solo 50 caracteres
#esta agenda o lista de contacto debe poder guardar o modificar la lista
#dicho esto resuelva las dificultades del caso



#la fundacion duoc uc solicia de sus servivicios profesionales para desarrollar un sistema que le permita almacenar los datos
#personales de cada uno de los estudiantes
#nombre,apellido,rut,correo electronico, carrera, 
# dentro de carrera van a tener la siguiente lista:
#ingeneria, analista, gastronomia

#materias por carrera:
#ingeneria: desarrolo web, desarrollo movil y desarrollo escritorio
#analista: analisis de datos, limpieza de datos, creacion de dashwork
#gastronomia: historia gastronomia, alimentos naturales y procesados, sopaipilla 2
# Lista para almacenar los estudiantes
estudiantes = []

# Ciclo para ingresar estudiantes
while True:
    print("Ingrese los datos del estudiante:")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    rut = input("RUT: ")
    correo = input("Correo electrónico: ")

    print("Carreras disponibles:")
    print("1. Ingeniería")
    print("2. Analista")
    print("3. Gastronomía")
    
    carrera = input("Seleccione una carrera (1-3): ")

    if carrera == "1":
        carrera_nombre = "Ingeniería"
        materias = ["Desarrollo Web", "Desarrollo Móvil", "Desarrollo Escritorio"]
    elif carrera == "2":
        carrera_nombre = "Analista"
        materias = ["Análisis de Datos", "Limpieza de Datos", "Creación de Dashwork"]
    elif carrera == "3":
        carrera_nombre = "Gastronomía"
        materias = ["Historia Gastronomía", "Alimentos Naturales y Procesados", "Sopaipilla 2"]
    else:
        print("Opción inválida. Intente nuevamente.")
        continue

    # Crear diccionario con los datos del estudiante
    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "rut": rut,
        "correo": correo,
        "carrera": carrera_nombre,
        "materias": materias
    }

    # Agregar estudiante a la lista
    estudiantes.append(estudiante)

    # Preguntar si se desea ingresar otro estudiante
    continuar = input("¿Desea ingresar otro estudiante? (si/no): ")
    if continuar.lower() != "si":
        break

# Mostrar los datos ingresados
print("\n--- Lista de Estudiantes ---")
for est in estudiantes:
    print(f"Nombre: {est['nombre']} {est['apellido']}")
    print(f"RUT: {est['rut']}")
    print(f"Correo: {est['correo']}")
    print(f"Carrera: {est['carrera']}")
    print("Materias:")
    for materia in est['materias']:
        print(f"- {materia}")
    print("-------------------------")


