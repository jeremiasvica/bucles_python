# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

from pickle import TRUE
print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

while True:
    nro1=float(input("primer numero:\n")) 
    nro2=float(input("segundo numero:\n"))
    print()
    operacion=str(input("operacion a realizar:\n"
    "suma (+)\n"
    "resta (-)\n"
    "multiplicacion (*)\n"
    "division (/)\n"
    "potencia (**)\n"
    "salir tipeando FIN\n"))
    if operacion == "+":
        suma=nro1+nro2
        print("El resultado de la suma es:", suma)
    elif operacion=="-":
        resta=nro1-nro2
        print("El resultado de la resta es:", resta)
    elif operacion=="*":
        multiplicacion=nro1*nro2
        print("El resultado de la multiplicacion es:", multiplicacion)
    elif operacion=="/":
        division=nro1/nro2
        print("El resultado de la multiplicacion es:", division)
    elif operacion=="**":
        potencia=nro1**nro2
        print("El resultado de la potencia es:", potencia)
    elif operacion=="FIN":
        break
    else:
        print("ingrese operador valido")
print()
print("")