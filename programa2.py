a = [10, 23, 14, 15]  # arreglo: convención de un solo tipo (números), tamaño definido - finito
                      # array: convention of single type (numbers), fixed size - finite
b = []                # lista: puede crecer y contener varios tipos - dinámica e "infinita"
                      # list: can grow and hold multiple types - dynamic and "infinite"

a[0] = 10             # cambia el primer valor de 'a' a 10 (aunque ya era 10)
                      # changes first value of 'a' to 10 (even though it was already 10)

b.append(12)          # agrega el valor 12 al final de la lista 'b'
                      # adds the value 12 to the end of list 'b'

# b = {"hola", 10, 10.05, False, 'm', {1, 2, 3, 4}} 
# línea comentada: esto no es una lista, es un 'set' (conjunto), y no permite listas dentro

# ciclos y comparación de tamaño
# loops and size comparison
if (len(a) > len(b)):
    print("A es mayor")
else: 
    print("B es mayor")

# repite 3 veces: i toma valores 0, 1, 2
# repeats 3 times: i takes values 0, 1, 2
for i in range(3):
    print(i)

# recorre cada elemento en 'a'
# iterates through each element in 'a'
for i in a:
    print(a)  # imprime toda la lista 'a' en cada vuelta → [10,23,14,15] repetido 4 veces
              # prints entire list 'a' each time → [10,23,14,15] repeated 4 times