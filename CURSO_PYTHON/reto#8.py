nombre = str(input("Cuál es tu nombre?"))
edad = int(input("Cuál es tu edad?"))

nota1 = float(input("ingresa tu primera nota:"))
nota2 = float(input("ingresa tu segunda nota:"))
nota3 = float(input("ingresa tu tercera nota:"))

promedio = (nota1 + nota2 + nota3) / 3



print("Hola, "+ nombre)
print("Tu edad es: ", edad)
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("Tu promedio es: ", promedio)
