# hacer un programa que en una lista se introducan cadenas de carcteres, con las siguietnes restriccines:
# make a program that inputs character strings into a list, with the following restrictions:
# -laas cedanas no deben tener espacios / strings must not have spaces
# -la cadena solo puede tener mayuscula la primer letra / only the first letter can be uppercase
# -obligatoriamente debe tener todas las vocales. / must contain all vowels
# El programa no termina hasta que la lista tenga 5 elementos / program doesn't end until list has 5 elements
def main():
    # crear una lista / create a list
    lis = []
    con = 0  # Contador de elementos válidos / Valid elements counter
    while (con < 5):
        es = True   # Flag para espacios / Space flag
        may = 0     # Contador de mayúsculas / Uppercase counter
        est = False # Flag para estructura válida / Valid structure flag
        voc = 0     # Contador de vocales encontradas / Vowel counter
        
        # pedir cadena / request string
        tem = input("Cadena: ")
        
        # Analizar cada carácter de la cadena / Analyze each character in the string
        for i in tem:
            # Verificar si es mayúscula (códigos ASCII 65-90)
            # Check if it's uppercase (ASCII codes 65-90)
            if ord(i) >= 65 and ord(i) <= 90:
                may += 1

        # Verificar presencia de cada vocal (mayúscula o minúscula)
        # Check presence of each vowel (uppercase or lowercase)
        if ("A"in tem) or ("a"in tem):
            voc += 1
        if ("E"in tem) or ("e"in tem):
            voc += 1
        if ("I"in tem) or ("i"in tem):
            voc += 1
        if ("O"in tem) or ("o"in tem):
            voc += 1
        if ("U"in tem) or ("u"in tem):
            voc += 1
            
        # Verificar si hay espacios / Check for spaces
        if " " in tem:
            es = False
            
        # Verificar estructura de mayúsculas:
        # Check uppercase structure:
        # - Solo una mayúscula y debe ser la primera letra
        # - Only one uppercase and it must be the first letter
        # - O ninguna mayúscula
        # - Or no uppercase
        if (may == 1) and (ord(tem[0]) >= 65 and ord(tem[0]) <= 90):
            est = True
        elif(may == 0):
            est = True
            
        # Verificar si cumple todas las condiciones / Check if all conditions are met
        if est and (voc == 5) and es:
            print("Valido")
            con += 1
            lis.append(tem)
    
    # Mostrar lista final con todas las cadenas válidas
    # Show final list with all valid strings
    print(lis)


if __name__=="__main__":
    main()