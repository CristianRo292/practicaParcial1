a = [10] # arreglo [solo un tipo de dato] - finito
b = [] # lista [multiples tipos de datos] - infinito

a[0] = 10

b.append(12)

# b = {"hola", 10, 10.05, False, 'm', {1, 2, 3, 4}} 

# ciclos 
if (len(a) > len(b)):
    print("A es mayor")

else: 
    print("B es mayor")

for i in range (3):
    print(i)

for i in a :
    print(a)