#Reto de semana 7, lista de alumnos con asignaturas y calificaciones.

def capturar_calificaciones():
    asignaturas = ["Matemáticas", "Física", "Química", "Biología"]
    calificaciones = {}

    while True:
        alumno = input("Ingrese el nombre del alumno (o 'fin' para terminar): ")
        if alumno.lower() == "fin":
            break

        cantidad = 0
        while cantidad < 1 or cantidad > 3:
            cantidad = int(input("¿Cuántas calificaciones va a ingresar? (1 a 3): "))

        calificaciones[alumno] = []

        for index in range(cantidad):
            print("Asignaturas disponibles:")
            print("1. Matemáticas")
            print("2. Física")
            print("3. Química")
            print("4. Biología")

            opcion = int(input("Seleccione la asignatura (1-4): "))
            calificacion = float(input("Ingrese la calificación: "))

            calificaciones[alumno].append(calificacion)

    print("\nPromedio por alumno:")
    for alumno in calificaciones:
        suma = sum(calificaciones[alumno])
        promedio = suma / len(calificaciones[alumno])
        print(alumno, ":", promedio)

    return calificaciones
capturar_calificaciones()