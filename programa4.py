# hacer unprograma que lea 10 numeros y los almacene en un arreglo
# make a program that reads 10 numbers and stores them in an array

a = []
s = 0
n = 0
numeros = "0,1,2,3,4,5,6,7,8,9" # tambien se puede: "123456789";
while(n < 10):

    b = input("escribe un numero: ")
    x = 0

    for i in b: # se recorre los elementos del numero
                # iterates through the elements of the number

        # if(ord(i) >= 48 and ord(i) <= 57): # se preguna si son numeros
        if i in numeros:                     # asks if they are numbers
            x += 1                         

    if len(b) == x:      # si todos cocuerda son numeros y se agregan a la lista
        a.append(int(b)) # if all the numbers match, they are added to the list
        n += 1
    else:
        print("El valor no es numero")
        
    

for i in a:
    print(i)
    s += i
#print(a) # imprime toda la lista, incluyendo los corchetes
          # prints the entire list, including the brackets

print(f"la suma es:{s}")