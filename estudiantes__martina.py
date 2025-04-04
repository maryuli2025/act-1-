estudiantes = {
    "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},
    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},
    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}

# Función para agregar un nuevo estudiante
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    materias = input("Ingrese las materias aprobadas (separadas por coma): ").split(",")
    estudiantes[nombre] = {"edad": edad, "materias": [materia.strip() for materia in materias]}
    print(f"Estudiante {nombre} agregado correctamente.")

# Función para mostrar todos los estudiantes
def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        for nombre, datos in estudiantes.items():
            print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {', '.join(datos['materias'])}")

# Función para eliminar un estudiante por nombre
def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado correctamente.")
    else:
        print("Estudiante no encontrado.")

# Función para buscar un estudiante por nombre
def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        datos = estudiantes[nombre]
        print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {', '.join(datos['materias'])}")
    else:
        print("Estudiante no encontrado.")

# Función para verificar si una palabra clave está en el nombre de algún estudiante
def verificar_palabra_clave():
    palabra = input("Ingrese una palabra clave para buscar en los nombres: ").lower()
    encontrados = [nombre for nombre in estudiantes if palabra in nombre.lower()]
    if encontrados:
        print("Estudiantes encontrados:")
        for nombre in encontrados:
            print(f"- {nombre}")
    else:
        print("No se encontraron estudiantes con esa palabra clave.")

# Menú principal
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar estudiante")
        print("2. Mostrar lista de estudiantes")
        print("3. Eliminar estudiante")
        print("4. Buscar estudiante")
        print("5. Verificar palabra clave en nombres")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                agregar_estudiante()
            case "2":
                mostrar_estudiantes()
            case "3":
                eliminar_estudiante()
            case "4":
                buscar_estudiante()
            case "5":
                verificar_palabra_clave()
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()