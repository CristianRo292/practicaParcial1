'''
hacer un programa que lea una cadena y que muestre en pantalla 
cuntos numero tiene, cuantas mayuscular, cuantas minusculas, y cuantos 
espacios
make a program that reads a string and displays on screen 
how many numbers it has, how many uppercase, how many lowercase, and how many 
spaces
'''
def main():
    # Inicializar contadores / Initialize counters
    mi = 0      # Contador de letras minúsculas / Lowercase letters counter
    may = 0     # Contador de letras mayúsculas / Uppercase letters counter
    c = 0       # Contador de números / Numbers counter
    e = 0       # Contador de espacios / Spaces counter
    
    # Cadena con todos los caracteres numéricos
    # String with all numeric characters
    num = "1234567890" # ["1","2","3","4","5","6","7","8","9","0"]
    
    # Solicitar entrada al usuario / Prompt user for input
    cadena = input("Escribe una cadena: \n")
    
    # Analizar cada carácter de la cadena / Analyze each character in the string
    for i in cadena:
        # Verificar si es número / Check if it's a number
        if i in num:
            c += 1  # Incrementar contador de números / Increment numbers counter

        # Verificar si es espacio / Check if it's a space
        if i == ' ':
            e += 1  # Incrementar contador de espacios / Increment spaces counter
            
        # Verificar si es letra minúscula (códigos ASCII 97-122)
        # Check if it's lowercase letter (ASCII codes 97-122)
        if ord(i) >= 97 and ord(i) <= 122:
            mi += 1  # Incrementar contador de minúsculas / Increment lowercase counter
        
        # Verificar si es letra mayúscula (códigos ASCII 65-90)
        # Check if it's uppercase letter (ASCII codes 65-90)
        if ord(i) >= 65 and ord(i) <= 90:
            may += 1  # Incrementar contador de mayúsculas / Increment uppercase counter
    
    # Mostrar resultados / Display results
    print(f"Los numeros son: {c}, y los espacion: {e}\n y las minuscular {mi}, y las mayusculas: {may}")





if __name__=='__main__':
    main()