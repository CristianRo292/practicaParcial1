# Inicializar arreglo de 10 elementos con valor -1
# Initialize array of 10 elements with value -1
arr = [-1]*10

# Inicializar lista vacía para caracteres
# Initialize empty list for characters
car = []
c = 0  # Contador para el número de entradas / Counter for number of inputs

# Bucle para capturar 10 entradas del usuario
# Loop to capture 10 user inputs
while (True):
    a = input("Escribe un dato o valor: ")
    
    # Verificar si la entrada es un número
    # Check if input is a number
    if a.isdigit(): 
        arr[c] = int(a)  # Almacenar número en el arreglo / Store number in array
    # Verificar si la entrada es alfabética
    # Check if input is alphabetic
    elif a.isalpha():
        car.append(a)  # Agregar carácter a la lista / Add character to list
    c += 1  # Incrementar contador de entradas / Increment input counter
    
    # Salir del bucle después de 10 entradas
    # Exit loop after 10 inputs
    if c >= 10:
        break

# Contar elementos válidos en el arreglo (no -1)
# Count valid elements in array (not -1)
c2 = 0
for i in arr:
    if i != -1:
        c2 += 1

# Mostrar resultados
# Display results
print(f"El arreglo tine {c2}")
print(arr)
print(f"La lista tiene {len(car)}")
print(car)