subjects = []
grades = []


def leerEstudiante():
    studentName = input("Ingrese el nombre del estudiante: ")
    return studentName


def elegirOpcion():

    print("\n--- REGISTRO DE ESTUDIANTES ---")
    print("1. Registrar asignatura y nota")
    print("2. Ver resultado del estudiante")

    while True:
        try:
            option = int(input("Seleccione una opción: "))

            if option == 1 or option == 2:
                return option

            else:
                print("Ingrese una opción entre 1 y 2.")

        except ValueError:
            print("Ingrese un valor numérico.")


def registrarNota():

    subject = input("Ingrese el nombre de la asignatura: ")

    while True:
        try:
            grade = float(input("Ingrese la calificación de la asignatura: "))

            if grade >= 0 and grade <= 100:

                subjects.append(subject)
                grades.append(grade)

                print("Nota registrada correctamente.")
                break

            else:
                print("La calificación debe estar entre 0 y 100.")

        except ValueError:
            print("Debe ingresar un valor numérico.")