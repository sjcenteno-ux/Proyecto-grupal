import grades as gra


def mostrarResultado(student, Classes, grades, average, performance):

    print("\n--- RESULTADO DEL ESTUDIANTE ---")
    print(f"Estudiante: {student}")

    print("\nAsignaturas y calificaciones:")

    for i in range(len(Classes)):

        subjectStatus = gra.estadoAsignatura(grades[i])
        recommendation = gra.recomendacion(grades[i])

        print(f"\n{Classes[i]}: {grades[i]} - {subjectStatus}")
        print(f"Recomendación: {recommendation}")

    print(f"\nPromedio general: {average:.2f}")
    print(f"Nivel de rendimiento: {performance}")