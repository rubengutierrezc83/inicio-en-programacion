#SISTEMA DE APROBACION DE NOTAS
#1. solicitar el nombre del estudiante
nombre=input("ingrese su nombre; ")

#2. solitar las tres notas
#float()convierte texto ingresado en un numero decimal

nota1=float(input ("valor de la nota1: "))
nota2=float(input ("valor de la nota2: "))
nota3=float(input ("valor de la nota3: "))

#3. calcular el promedio de las tres notas

promedio=(nota1+nota2+nota3) /3

#resultado

print("el promedio es ", promedio) 


# 4. Mostrar la información del estudiante
print("\n===== RESULTADO ACADÉMICO =====")
print("nombre del estudiante: ", nombre) 
print("promedio: ", round(promedio, 2)) 
# 5. Evaluar el promedio usando condicionales
# si el promedio >=3.0 aprobado
if promedio >=4.5:
    print("resultado le fue excelente")
elif promedio >=3.0:
    print("resultado le fue bien")
# si el promedio e<3.0 reprobado
else:
    print("resultado reprobado")
    
    