# # intrucciones de entrada y salida:
# # print() o print(f"")
# print ("Hola mundo")
# print (f"hola mundo {10}")

# # Entrada de datos 
# input("Escribe un numero: ") # Se introsucen solamente carcateres
# # casting para convertir caracteres en valores especificos 
# f = 1.00
# f = float(input("Escribe un numero con decimales"))
# a = 0
# a = int(input("Escribe un numero"))
# c = 120
# print(str(c))
# v = ""
# v = str(c)
# # nota: Solo las variables que no se introducen por teclado se obliga a inicializarlas

'''
hacer un programa que lea nombre y precio de un producto, el programa calculara el 
costo y precio de venta 
el costo involucra el 12% y  el iva el 16% 

make a program that reads the name and price of a product, the program will calculate the 
cost and sale price
the cost involves 12% and VAT 16%
'''

def main():
   # while(True): 
    # Bucle para procesar 5 productos / Loop to process 5 products
    for i in range(0,5): # rango, tiene valor inicial y valor final / range has start and end value
        # pedir nombre / request name
        prod = input("Nombre producto: \n")
        # pedir precio / request price
        precioB  = input("Precio primario: ")
        # Validar que el precio sea un número válido
        # Validate that the price is a valid number
        if validar(precioB): 
            # calcular el preio final / calculate final price
            # sumarle 12% mas 16% / add 12% plus 16%
            costo = float(precioB) * 1.12  # Calcular costo con 12% / Calculate cost with 12%
            preciof = costo * 1.16         # Calcular precio final con 16% IVA / Calculate final price with 16% VAT

            # Mostrar resultados con formato de 2 decimales
            # Show results with 2 decimal format
            print(f"El producto: {prod},tiene un costo de: {costo:.2f}, tiene un precio de venta de: {preciof:.2f}")
            # ":.2F" configura que el flotante solo tenga 2 decimales(los trunca)
            # ":.2F" configures the float to have only 2 decimals (truncates them)
        else:
            print("Precio no valido ")  # Mensaje de error / Error message

        # resp = input("Desea otro numero (s/n) \n")

        # if resp == "n" or resp == "N":
        # if resp in ["n","N"]:
        #      break

# Función para validar si una cadena puede convertirse a número
# Function to validate if a string can be converted to a number
def validar(num):
    try:
        nuevoN = float(num)  # Intentar convertir a flotante / Try to convert to float
        return True          # Retornar verdadero si es válido / Return true if valid
    
    except:
        return False         # Retornar falso si hay error / Return false if error

# Punto de entrada del programa
# Program entry point
if __name__ == "__main__":
    main()
