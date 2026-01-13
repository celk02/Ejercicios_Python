print("Duelo de Paciencia")
print("Se más paciente que yo")


for i in range(10):
    numero = int(input(f"i {i +1}: inserta cualquier numero diferente a {i}: "))

    if numero == i:
        print(f"Oye,!no debias escribir a {i}!")
        break


    if i==9:
        print("Vaya, eres más paciente que yo, ganaste")

