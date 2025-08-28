# hacer un programa que lea 10 numeros y los almacene en un arreglo
# make a program that reads 10 numbers and stores them in an array
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 1: arreglo de 10 posiciones, inicializado en cero
# 1: array of 10 positions, initialized to zero
# 2: se llenará con los números ingresados por el usuario
# 2: will be filled with numbers entered by the user

# bucle que recorre dentro de un rango de 0 a 9 (10 posiciones)
# loop that iterates over the range 0 to 9 (10 positions)
for i in range(0, 10):
    num[i] = int(input(f"Escribe un numero {i + 1}: \n "))

# imprime cada número almacenado en el arreglo
# prints each number stored in the array
for i in num:
    print(i)