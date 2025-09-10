# def validar(tex):
#     c = 0
#     d = 0.0

#     try: 
#         c = int(tex) # si se puede convertir en int es un numero
#         print("Es un valor numerico, sin decimal")  # It's a numeric value without decimals
#     except ValueError: # si hay error de conversion 
#         print("No es un valor numerico sin decimales")  # Not a numeric value without decimals
    
#     try: 
#         d = float(tex) # si se puede convertir a float es un flotante
#         print("Es un valor numerico con decimales")  # It's a numeric value with decimals
#     except ValueError:
#         print("No es un valor numerico con decimales ")  # Not a numeric value with decimals

# def leer():
#     # ord() --> obtiene el ascii del caracter   # ord() --> gets the ASCII value of the character
#     # .isalpha --> para carcteres               # .isalpha --> checks if it's a letter
#     # .isdigit --> para numeros                 # .isdigit --> checks if it's a number
#     # try except valueError: 
#     a = input("Ecribe un dato o valor: \n") # resivimos datos  # Receive data from user
#     validar(a) # mandamos a validar los datos  # Send data to validate

'''
Hacer un programa que lea un dato cual quiera, y que lo almacene en una lista respetando su tipo de dato
Create a program that reads any input and stores it in a list respecting its data type
'''

def valnum(tem):
    n = 0.0
    if tem.isdigit():
        print("Es int")  # It's an integer
        lista.append(int(tem))  # Add integer to the list / Agregar entero a la lista
        return True
    else:
        try:
            n = float(tem)
            print("Es float")  # It's a float
            lista.append(n)  # Add float to the list / Agregar float a la lista
            return True
        except ValueError:
            return False  # Not a number / No es un número
            

def leer():
    tem = input("Dato: ")  # Ask user for input / Pedir dato al usuario
    
    if valnum(tem) == False:
        print("Es Str")  # It's a string / Es una cadena
        lista.append(tem)  # Add string to the list / Agregar cadena a la lista
    

lista = []  # List to store all inputs / Lista para almacenar todos los datos

if __name__ == "__main__":
    while(True):
        leer()  # Call the read function / Llamar función leer
        r = input("Desea agregar otro numero:(s/n)\n")  # Ask if user wants to continue / Preguntar si quiere continuar

        if (r in ["n","N"]):
            print(lista)  # Print the final list / Imprimir la lista final
            break
