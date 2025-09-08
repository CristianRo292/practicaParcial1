# Función para verificar si una cadena contiene todas las vocales
# Function to check if a string contains all vowels
def vocales(cad):
    # Bandera para cada vocal (inicialmente falsas)
    # Flag for each vowel (initially false)
    ba = False
    be = False
    bi = False
    bo = False
    bu = False

    # Verificar presencia de cada vocal (mayúscula o minúscula)
    # Check presence of each vowel (uppercase or lowercase)
    if "a" in cad or "A" in cad:
        ba = True
    if "e" in cad or "E" in cad:
        be = True
    if "i" in cad or "I" in cad:
        bi = True
    if "o" in cad or "O" in cad:
        bo = True
    if "u" in cad or "U" in cad:
        bu = True

    # Si todas las vocales están presentes, agregar cadena a la lista
    # If all vowels are present, add string to list
    if ba and be and bi and bo and bu:
        lista.append(cad)
    
    # Mostrar estado actual de la lista
    # Show current state of the list
    print(f"La lista es: {lista}")

# Función para verificar que solo la primera letra es mayúscula
# Function to verify that only the first letter is uppercase
def minusculas(c1):
    print(c1)
    cm = 0  # Contador de letras minúsculas / Lowercase letters counter
    
    # Verificar que todos los caracteres excepto el primero son minúsculas
    # Verify that all characters except the first are lowercase
    for i in c1[1:]:
        if ord(i) >= 97 and ord(i) <= 122:  # Códigos ASCII para letras minúsculas
            cm += 1                         # ASCII codes for lowercase letters
            
    # Si todos los caracteres después del primero son minúsculas
    # If all characters after the first are lowercase
    if cm == len(c1) - 1:
        print(f"La cadena son minusculas exepto la primera{cm}")
        vocales(cm)  # Llamar a función de verificación de vocales / Call vowel check function
    else:
        print("Error la cadena no cumple")

# Función principal del programa
# Main program function
def main():
    ce = 0  # Contador de caracteres no espacio / Non-space character counter
    nc = "" # Cadena para almacenar caracteres no numéricos / String to store non-numeric characters
    
    c = input("Escribe una cadena: \n")
    
    # Contar caracteres que no son espacios
    # Count characters that are not spaces
    for i in c:
        if ord(i) != 32:  # 32 es código ASCII para espacio / 32 is ASCII code for space
            ce += 1

    # Verificar si la cadena no contiene espacios
    # Check if the string contains no spaces
    if (ce == len(c)):
        # Si la cadena es completamente alfabética
        # If the string is completely alphabetic
        if c.isalpha():
            # Revisar que solo la primera letra sea mayúscula
            # Check that only the first letter is uppercase
            minusculas(c)
        else:
            # Filtrar solo caracteres no numéricos
            # Filter only non-numeric characters
            for i in c: 
                if ord(i) >= 48 and ord(i) <= 57:  # Códigos ASCII para dígitos 0-9
                    pass                           # ASCII codes for digits 0-9
                else:
                    nc += i
            minusculas(nc)  # Verificar la cadena filtrada / Check the filtered string
    else:
        print("Error la cadena no cumple")

# Lista global para almacenar cadenas válidas
# Global list to store valid strings
lista = []

# Punto de entrada del programa
# Program entry point
if __name__=="__main__":
    # Bucle hasta que la lista tenga 5 elementos válidos
    # Loop until the list has 5 valid elements
    while(True):
        main()
        if len(lista) >= 5:
            break