nombre= input("Ingresa tu numbre: ")
apellido= input("Ingresa tu apellido: ")

nombre_completo = nombre + " " + apellido
print(f"nombre_completo: {nombre_completo}")

vocales= "aeiouAEIOU"
nombre_z= ""

for a in nombre_completo:
    if a in vocales:
        nombre_z += "z"
    else: 
        nombre_z += a
print(f"vocales remplezadas por 'z': {nombre_z}")



nombre_alreves = nombre_completo [::-1]
print(f"nombre_alreves: {nombre_alreves}")