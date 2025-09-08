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
        es = 0      # Contador de espacios / Space counter
        may = 0     # Contador de mayúsculas / Uppercase counter
        est = False # Flag para estructura válida / Valid structure flag
        # Contadores individuales para cada vocal
        # Individual counters for each vowel
        a = 0
        e = 0
        iv = 0  # 'iv' para evitar conflicto con la variable de iteración 'i'
        o = 0   # 'iv' to avoid conflict with iteration variable 'i'
        u = 0
        
        # pedir cadena / request string
        tem = input("Cadena: ")
        
        # Analizar cada carácter de la cadena / Analyze each character in the string
        for i in tem:
            # Verificar espacios / Check for spaces
            if i == ' ':
                es += 1
            # Verificar mayúsculas (códigos ASCII 65-90)
            # Check for uppercase (ASCII codes 65-90)
            if ord(i) >= 65 and ord(i) <= 90:
                may += 1
            # Contar ocurrencias de cada vocal (mayúscula y minúscula)
            # Count occurrences of each vowel (uppercase and lowercase)
            if i in ["a","A"]:
                a += 1
            if i in ["e","E"]:
                e += 1
            if i in ["i","I"]:
                iv += 1
            if i in ["o","O"]:
                o += 1
            if i in ["u","U"]:
                u += 1
                
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
            
        # Verificar si cumple todas las condiciones:
        # Check if all conditions are met:
        # - Estructura de mayúsculas válida / Valid uppercase structure
        # - Todas las vocales presentes al menos una vez / All vowels present at least once
        # - Sin espacios / No spaces
        if est and (a != 0) and (e != 0) and(iv != 0) and(o != 0) and (u != 0) and (es == 0):
            print("Valido")
            con += 1
            lis.append(tem)
            
    # Mostrar lista final con todas las cadenas válidas
    # Show final list with all valid strings
    print(lis)


if __name__=="__main__":
    main()