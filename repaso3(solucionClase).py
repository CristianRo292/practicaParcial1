def validar(a):
    ne = 0
    try:
        ne = int(a)  # Intentar convertir a entero / Try to convert to integer
        return ne    # Retornar entero / Return integer
    except ValueError:
        print("No es un entero")  # No se pudo convertir a entero / Not an integer
    
    try: 
        nf = float(a)  # Intentar convertir a flotante / Try to convert to float
        return nf      # Retornar flotante / Return float
    except ValueError:
        print("No es un decimal")  # No se pudo convertir a flotante / Not a float
    
    return a  # Si no es número, retornar como string / If not a number, return as string

def leer():
    a = input("Escribe un dato \n")  # Pedir dato al usuario / Ask the user for input
    dato = validar(a)                # Validar el dato ingresado / Validate the input
    lista.append(dato)               # Agregar el dato a la lista / Append the data to the list

lista = []  # Lista para almacenar los datos / List to store all inputs

if __name__ == "__main__":
    while(True):
        leer()  # Llamar función leer / Call read function
        res = input("Deseas otros/n: \n")  # Preguntar si desea continuar / Ask if the user wants to continue
        if res == "n" or res == "N": 
            print(lista)  # Imprimir lista final / Print final list
            break
