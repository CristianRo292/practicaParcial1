'''
hacer un programa que lea 10 datos, si el dato es un numero, se almacenara en un arreglo
si es un carcater o caracteres se metera en una lista, cuando finalice el programa nos mostrara 
cuantos elemtos numericos y cuantos carateres hay en cada estructura
'''

# declarar los arreglos y la lista
# declare the arrays and the list
# num = [0,0,0,0,0,0,0,0,0,0] # arreglo fijo de 10 posiciones para números (inicializado con ceros)
num = [0]*10                  # fixed array of 10 positions for numbers (initialized with zeros)
pos = 0                       # posición actual en el arreglo 'num' (cuántos números llevamos guardados)
                              # current position in the 'num' array (how many numbers we have stored)
cract = []                    # lista para almacenar caracteres o cadenas de texto
                              # list to store characters or text strings

# preguntar 10 datos
# ask for 10 data inputs
n = 0                         # contador de datos ingresados (de 0 a 9)
                              # counter for entered data (from 0 to 9)
while(n < 10):
    aux = input("datos: ")    # leer entrada del usuario
                              # read user input
    cont = 0                  # variable no utilizada (podría eliminarse, pero no se modifica el código)
                              # unused variable (could be removed, but code is not modified)

    # ver si es caracter o numero
    # check if it is a character or a number
    if aux.isdigit():         # si todos los caracteres son dígitos (ej: "123", válido como número)
                              # if all characters are digits (e.g., "123", valid as number)
       num[pos] = int(aux)    # convertir a entero y guardarlo en la posición actual de 'num'
                              # convert to integer and store in current 'num' position
       pos += 1               # avanzar a la siguiente posición en el arreglo
                              # move to the next position in the array
       n += 1                 # aumentar el contador de datos ingresados
                              # increase the entered data counter

    elif aux.isalpha():       # si todos los caracteres son letras (ej: "hola", "abc")
                              # if all characters are letters (e.g., "hola", "abc")
        cract.append(aux)     # agregar el texto a la lista de caracteres
                              # add the text to the characters list
        n += 1                # aumentar el contador de datos ingresados
                              # increase the entered data counter

    else:   # si no es ni número ni solo letras (ej: "12a", "@", "1.5")
            # if it's neither number nor only letters (e.g., "12a", "@", "1.5")
        print("No valido")  # mostrar mensaje de error
                            # show error message

# mostrar resultados finales
# display final results
print(f"cantidad de numeros: {pos}")  # total de números válidos guardados
                                      # total valid numbers stored
# print(f"Numeros ingresados: {num[:pos]}")
print(f"cantidad de caracteres: {len(cract)}") # total de cadenas de texto (solo letras) ingresadas
                                               # total text strings (only letters) entered
# print(f"String ingresados: {cract}")
