
def say_hello(numero):
    for i in range(numero):
        print("Hello")
say_hello(5)
print()


def multiplicar(a,b):
    return a * b

num1= float(input("ingrese el primer numero: "))
num2= float(input("ingrese el segundo numero: "))
resultado = multiplicar (num1,num2)
print("multiplicar es: ", resultado)


# imprimir el numero recibido, y que lo divida entre dos y se llame recursivamente mientras que el numero sea mayor que 0
def half(numero):
    print(int(numero))
    if numero >=0 :
        half(numero/2)
half(100)

    