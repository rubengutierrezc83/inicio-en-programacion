# SISTEMA DE APROBACION DE NOTAS

# 1. solicitar el nombre del estudiante
nombre = input("ingrese su nombre; ")

# 2. solitar las tres notas
nota1 = float(input("valor de la nota1: "))
nota2 = float(input("valor de la nota2: "))
nota3 = float(input("valor de la nota3: "))

#3. Solicitar el porcentaje de las asistencias
asistencias = float(input("Porcentaje de asistencia (0-100): "))

#4. Preguntat si hizo el trabajo?
trabajo = input("¿Entego el trabajo final? (si/no)): ")

# lower: funcion que vuelve minusculas las letras
trabajo = trabajo.lower()

# Convertir el texto en un booleano
entrego_trabajo = trabajo == "si"

# 5. Evaluar el promedio
promedio = (nota1+nota2+nota3) /3

# 6. Mostrar la información del estudiante
print("\n===== RESULTADO ACADÉMICO =====")
print("nombre del estudiante: ", nombre)
print("promedio: ", round(promedio, 2))
print(f"Asistencias {asistencias} %")

# promedio >= 4.50 and asistencia >=80
if promedio >= 4.5 and asistencias >=  80:
    print("El estudiante fue Excelente")
elif promedio >= 3.5 and asistencias >= 70 and entrego_trabajo:
    print("El estudiante Aprobo")
else:
    print("requiere revisar con acudiente.")