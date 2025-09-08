# Definicion de un metodo / Method definition
def resultado():
     c2 = 0
     print(f"La lista tiene {len(car)}")
     # Contar elementos válidos en el arreglo (no -1)
     # Count valid elements in array (not -1)
     for i in arr:
        if i != -1:
            c2 += 1
     print(f"El arreglo tine {c2}")
     print(arr)
     print(car)

def hola():
    c = 0
    print("Hola mundo")
    # Bucle principal para capturar 10 entradas
    # Main loop to capture 10 inputs
    while (True):
        a = input("Escribe un dato o valor: ")
        
        # Validar si es número y almacenar en arreglo
        # Validate if number and store in array
        if a.isdigit(): 
            arr[c] = int(a)
        # Validar si es texto y almacenar en lista
        # Validate if text and store in list
        elif a.isalpha():
            car.append(a)
        c += 1
        # Condición de salida después de 10 entradas
        # Exit condition after 10 inputs
        if c >= 10:
            break

    resultado()

# variables globales o publicas / Global or public variables
# Arreglo pre-inicializado con valores -1
# Pre-initialized array with -1 values
arr = [-1]*10
# Lista vacía para caracteres / Empty list for characters
car = []


# llamado a metodo principal / Main method call
if __name__=="__main__":
    hola()