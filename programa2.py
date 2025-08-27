# hacer unprograma que lea 10 numeros y los almacene en un arreglo
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 1
# 2
for i in range (0,10):
    num[i] = int(input(f"Escribe un numero {i + 1}: \n "))

for i in num:
    print(i)