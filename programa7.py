'''
hacer un programa que lea nombre, edad y sexo de 5 personas, estos elementos tiene que estar dentro de una lista
make a program that reads name, age and gender of 5 people, these elements must be inside a list
'''
# .upper convierte a mayuscula / .upper converts to uppercase

# Lista para almacenar todos los registros de personas
# List to store all person records
registros = []
# persona = []
# def exper():
#     persona = {
#         "nombre": 'juan',
#         "edad": 12,
#         "sexo" : 'H'
#     }
#     print(persona)

def main():
    # exper()
    n = 0  # Contador de personas registradas / Person counter
    # Bucle para registrar 5 personas / Loop to register 5 people
    while (n < 5):
        temp = input("Nombre: ")
        # Validar que el nombre contenga solo letras
        # Validate that name contains only letters
        if temp.isalpha(): 
            nombre = temp
            temp = input("Edad: ")
            # Validar que la edad sea un número
            # Validate that age is a number
            if temp.isdigit():
                edad = int(temp)
                temp = input("Sexo: ")
                # Validar que el sexo contenga solo letras
                # Validate that gender contains only letters
                if temp.isalpha():
                    sex = temp

                    # Crear cadena con información de la persona
                    # Create string with person information
                    aux = "Nombre: " + nombre + ", Edad: " + str(edad) + ", Sexo: " + sex
                    # Agregar persona a la lista de registros
                    # Add person to the records list
                    registros.append(aux)
                    n += 1  # Incrementar contador de personas
                    # registros.pop # borra toda la lista / deletes the entire list
                else: 
                    print("Sexo no valido")
            else:
                print("Edad no valida")
        else:
            print("Nombre no valido")

    # Mostrar todos los registros al final
    # Display all records at the end
    print(registros)



if __name__=="__main__":
    main()