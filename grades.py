MinimunPassingGrade = 70


def calcularPromedio(grades):
    if len(grades) == 0:
        return 0

    total = 0
    validCount = 0

    for grade in grades:

        if type(grade) == int or type(grade) == float:

            if grade >= 0 and grade <= 100:
                total = total + grade
                validCount = validCount + 1

    if validCount == 0:
        return 0

    average = total / validCount

    return average


def estadoAsignatura(grade):

    if grade >= MinimunPassingGrade:
        return "Aprobada"

    else:
        return "Reprobada"


def nivelRendimiento(average):

    if average <= 69:
        return "Aprendizaje inicial"

    elif average <= 79:
        return "Aprendizaje fundamental"

    elif average <= 89:
        return "Aprendizaje satisfactorio"

    else:
        return "Aprendizaje avanzado"


def recomendacion(grade):

    if grade <= 69:
        return "Debe reforzar los contenidos y practicar más."

    elif grade <= 79:
        return "Debe continuar practicando para mejorar su rendimiento."

    elif grade <= 89:
        return "Buen rendimiento. Puede seguir fortaleciendo sus conocimientos."

    else:
        return "Excelente rendimiento. Continúe manteniendo este nivel."